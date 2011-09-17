from flask.views import View
from flask import request, render_template, abort


class ListView(View):

    def __init__(self, template_name):
        self.template_name = template_name

    def render_template(self, context):
        return render_template(self.template_name, **context) #unpack context
    
    def get_context(self):
        """Should return a dictionary."""
        raise NotImplementedError()

    def dispatch_request(self):
        context = {}
        context.update(self.get_context())
        return self.render_template(context)


class PaginatedListView(ListView):
    
    methods = ['GET']

    def __init__(self, model, template_name, paginate_by=25):
        self.model = model
        self.ctype = self.model.__name__.lower()
        self.template_name = template_name
        self.paginate_by = paginate_by

    def paginate(self):
        ctxt = {'type': self.ctype}

        page = int(request.args.get('p', 1))
        
        obj_count = self.model.query.count()
        num_pages = obj_count / self.paginate_by

        if not obj_count: #we can't do anything without objects
            ctxt['error'] = "There are no '%s' in the database, make sure to add some." % self.ctype
            return ctxt

        if obj_count % self.paginate_by > 0:
            num_pages += 1

        if page < 1 or page > num_pages:
            return abort(404)
       
        objects = self.model.query.order_by('title').limit(self.paginate_by).offset((page - 1) * self.paginate_by)

        ctxt.update({
            'entries' : objects,
            'current_page' : page,
            'num_pages' : num_pages,
        })
        return ctxt
        
    def get_context(self):
        return self.paginate()
        
