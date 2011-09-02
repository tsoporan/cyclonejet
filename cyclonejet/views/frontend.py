# -*- encoding:utf-8 -*-
from flask import Module

frontend = Module(__name__)

@frontend.route('/')
def index():
    return "Hello,world"
