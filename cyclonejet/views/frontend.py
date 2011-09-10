# -*- encoding:utf-8 -*-
from flask import Module, url_for, redirect, \
        g, flash, request, current_app

#from cyclonejet.models import Anime

frontend = Module(__name__)

@frontend.route('/')
def index():
    return "Hello,world"
