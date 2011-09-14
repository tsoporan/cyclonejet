# -*- encoding:utf-8 -*-

class Config(object):
   
    DEBUG = True #for devel

    SECRET_KEY = 'U9F\'a[U\\:byA;N_^OGX5WG+|Nx|xf6"^'

    #SQLAlchemy Settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

    #WTForms Settings
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = '_csrf_token'
