#!/usr/bin/env python2
# -*- encoding:utf-8 -*-

from flask import current_app
from flaskext.script import Manager
from cyclonejet import create_app
from cyclonejet.extensions import db
from cyclonejet.models import User, Anime, Manga

app = create_app('cyclonejet')
manager = Manager(app)

@manager.command
def create_db():
    db.create_all()

@manager.command
def drop_db():
    db.drop_all()

def import_json(fp, model_class):

    import os
    assert os.path.exists(fp), "That file path doesn't seem to exist."

    try:
        import simplejson
        entries = simplejson.load(open(fp))
    except: # this needs to be json
        raise

    user = User.query_class.create_user(
            username='cyclonejet',
            email='jet@cyclonejet.com',
            password='changeme'
    )

    for e in entries:

        # this could be cleaned up a bit once we have the mangareader
        # spider returning cleaner data - @scjudd

        if model_class.__name__ == 'Manga':
            try:
                description = e['description'][0],
            except IndexError:
                description = e['description'],

            entry = model_class(
                title = e['title'],
                description = description,
                year = e['year'],
                author = e['author']
            )
        elif model_class.__name__ == 'Anime':
            entry = model_class(
                title = e['title'],
                description = e['description']
            )
        else:
            raise

        entry.user = user
        db.session.add(entry)

        try:
            db.session.commit()
        except Exception, e: # these are most-likely dupes
            print(e.message)
            db.session.rollback()

        try:
            print('Added {}: {}'.format(entry.__class__.__name__, entry.title))
        except UnicodeEncodeError:
            print('Added {}: {}'.format(entry.__class__.__name__, '[Error: UnicodeEncodeError]'))

    print('All done!')


@manager.command
def populate_anime(fp):
    """ Populate the Anime database from json. """
    import_json(fp, Anime)


@manager.command
def populate_manga(fp):
    """ Populate the Manga database from json. """
    import_json(fp, Manga)


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
