#!/usr/bin/env python2
# -*- encoding:utf-8 -*-

from flask import current_app
from flaskext.script import Manager
from cyclonejet import create_app
from cyclonejet.extensions import db
from cyclonejet.models import User, Anime

app = create_app()
manager = Manager(app)

@manager.command
def create_db():
    db.create_all()

@manager.command
def drop_db():
    db.drop_all()


#prefill our shell with some defaults
@manager.shell
def make_shell_context():
    return dict(
        app=current_app, 
        db=db,
        User=User,
        Anime=Anime,
    )

if __name__ == "__main__":
    manager.run()
