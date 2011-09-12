# -*- encoding:utf-8 -*-
from flask import Flask, render_template

from cyclonejet.views.frontend import frontend

from flaskext.sqlalchemy import SQLAlchemy
import settings

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.DB_URI

#Blueprint registration
app.register_blueprint(frontend)

#DB intialization
db = SQLAlchemy(app)


#Custom Error handling (move this somewhere else?)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


