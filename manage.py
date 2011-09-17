#!/usr/bin/env python2
# -*- encoding:utf-8 -*-

from flask import current_app
from flaskext.script import Manager, prompt_bool
from cyclonejet import create_app
from cyclonejet.extensions import db
from cyclonejet.models import User, Profile, Anime, Manga

app = create_app('cyclonejet')
manager = Manager(app)

@manager.command
def create_user(username, email, password):
    """
    Will create a user from supplied cli arguments.
    Since 'create_user' knows to check for an existing user first
    this will not create more than one of the same users.
    """
   
    try:
        user = User.query_class.create_user(
            username=username,
            email=email,
            password=password,
        )
        print('Created (or existing) user: %s' % user.username)
    except Exception, e:
        print(e)


@manager.command
def create_db():
    db.create_all()

@manager.command
def drop_db():
    if prompt_bool('Are you sure you want to destroy all your data?'):
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

        for i in e.iterkeys():
            if type(e[i]).__name__ in ['list','tuple']:
                try:
                    e[i] = e[i][0]
                except IndexError:
                    e[i] = ''

        if model_class.__name__ == 'Manga':
            entry = model_class(
                title = e['title'],
                description = e['description'],
                year = e['year'],
                author = e['author'],
            )
        elif model_class.__name__ == 'Anime':
            entry = model_class(
                title = e['title'],
                description = e['description'],
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
        Profile=Profile,
        Anime=Anime,
        Manga=Manga,
    )

if __name__ == "__main__":
    manager.run()
