#!/usr/bin/env python2
# -*- encoding:utf-8 -*-

from flask import current_app
from flaskext.script import Manager
from cyclonejet import create_app
from cyclonejet.extensions import db
from cyclonejet.models import User, Anime

app = create_app('cyclonejet')
manager = Manager(app)

@manager.command
def create_db():
    db.create_all()

@manager.command
def drop_db():
    db.drop_all()

@manager.command
def populate_anime(fp):
    """ Populate the Anime database from json. """

    import os
    assert os.path.exists(fp), "That file path doesn't seem to exist."

    try:
        import simplejson
        animes = simplejson.load(open(fp))
    except: #this needs to be json
        raise

    user = User.query_class.create_user(
            username='cyclonejet',
            email='jet@cyclonejet.com',
            password='changeme'
    )

    for a in animes:
        anime = Anime(
            title = a['title'],
            description = a['description'],
        )
        anime.user = user
        db.session.add(anime)
        
        try:
            db.session.commit()
        except Exception, e: #these are most-likely dupes
            print(e.message)
            db.session.rollback()

        print('Added anime: {}'.format(anime.title))

    print('All done!')




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
