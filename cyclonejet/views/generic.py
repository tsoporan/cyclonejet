from flask.views import View
from flask import request, render_template, abort


class ListView(View):

    def __init__(self, template_name):
        self.template_name = template_name

    def render_template(self, context):
        return render_template(self.template_name, **context) #unpack context
    
    def get_objects(self):
        raise NotImplementedError()

    def dispatch_request(self):
        context = {}
        context.update(self.get_objects())
        return self.render_template(context)

class PaginatedListView(ListView):
    methods = ['GET']

    PAGINATE_PER_PAGE = 25

    def __init__(self, model, template_name):
        self.CLS = model
        self.template_name = template_name

    def paginate(self):
        
        page = int(request.args.get('p', 1))
        
        obj_count = self.CLS.query.count()
        num_pages = obj_count / self.PAGINATE_PER_PAGE

        if obj_count % self.PAGINATE_PER_PAGE > 0:
            num_pages += 1

        if page < 1 or page > num_pages:
            return abort(404)
       
        objects = self.CLS.query.order_by('title').limit(self.PAGINATE_PER_PAGE).offset((page - 1) * self.PAGINATE_PER_PAGE)

        return {
            'entries' : objects,
            'current_page' : page,
            'num_pages' : num_pages,
        }
        
    def get_objects(self):
        return self.paginate()
        
