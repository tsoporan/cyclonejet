"""
Script for quickly populating the Anime database from a json file. 

For more information see scrapers.
"""


import os

import argparse
import simplejson

from cyclonejet.models import Anime
from cyclonejet.models import User
from cyclonejet import db

parser = argparse.ArgumentParser(description="Populate the Anime database from json.")
parser.add_argument('file_path', metavar='fp', action='store', help='The file path to the json file.')

args = parser.parse_args()

fp = args.file_path

assert os.path.exists(fp), "That file path doesn't seem to exist."

try:
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
    anime.uploader = user

    db.session.add(anime)
    try:
        db.session.commit()
    except Exception, e: #these are most-likely dupes
        print(e.message) 
        db.session.rollback()
    
    print('Added anime: {}'.format(anime.title))

print('All done!')
    

