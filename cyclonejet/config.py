# -*- encoding:utf-8 -*-

class Config(object):
   
    DEBUG = True #for devel

    SECRET_KEY = 'U9F\'a[U\\:byA;N_^OGX5WG+|Nx|xf6"^'

    #SQLAlchemy Settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

    #WTForms Settings
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = '_csrf_token'

    #Flask Mail settings
    MAIL_SERVER = 'localhost' 
    MAIL_PORT =  25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_DEBUG = DEBUG
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    DEFAULT_MAIL_SENDER = None
