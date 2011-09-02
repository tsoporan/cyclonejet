# -*- encoding:utf-8 -*-
from flask import Flask
from cyclonejet.views.frontend import frontend

app = Flask(__name__)
app.register_module(frontend)

