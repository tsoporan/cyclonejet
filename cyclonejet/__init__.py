# -*- encoding:utf-8 -*-
from flask import Flask
from cyclonejet.views.frontend import frontend
from flaskext.sqlalchemy import SQLAlchemy
import settings


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.DB_URI
app.register_module(frontend)

db = SQLAlchemy(app)
