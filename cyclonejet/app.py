from flask import Flask, render_template
from cyclonejet.views.frontend import frontend
from cyclonejet.views.anime import anime
from cyclonejet.views.manga import manga
from cyclonejet.views.accounts import accounts

from cyclonejet.extensions import db
from cyclonejet.extensions import mail

from cyclonejet.config import Config

def create_app(name):
    app = Flask(name)
    
    app.config.from_object(Config)

    #Blueprint registration
    app.register_blueprint(frontend)
    app.register_blueprint(accounts)
    app.register_blueprint(anime, url_prefix='/anime')
    app.register_blueprint(manga, url_prefix='/manga')

    #DB intialization
    db.init_app(app)
    
    #Mail initialization
    mail.init_app(app)

    #Custom Error handling (move this somewhere else?)
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    return app

