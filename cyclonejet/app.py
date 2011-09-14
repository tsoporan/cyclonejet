from flask import Flask, render_template
from cyclonejet.views.frontend import frontend
from cyclonejet.extensions import db

from cyclonejet.models import User, Anime

from cyclonejet.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    #Blueprint registration
    app.register_blueprint(frontend)

    #DB intialization
    db.init_app(app)

    #Custom Error handling (move this somewhere else?)
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    return app

