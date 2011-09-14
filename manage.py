#!/usr/bin/env python2
# -*- encoding:utf-8 -*-

from flask import current_app
from flaskext.script import Manager
from cyclonejet import create_app
from cyclonejet.extensions import db

app = create_app()
manager = Manager(app)

@manager.command
def create_db():
    db.create_all()

@manager.command
def drop_db():
    db.drop_all()


if __name__ == "__main__":
    manager.run()
