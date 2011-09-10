import sys
import os

import argparse
import simplejson

from cyclonejet.models.animes import Anime
from cyclonejet.models.tags import Tag

parser = argparse.ArgumentParser(description="Populate the Anime database from json.")
parser.add_argument('file_path', metavar='fp', action='store', help='The file path to the json file.')

args = parser.parse_args()

fp = args.file_path

assert os.path.exists(fp), "That file path doesn't seem to exist."

try:
    js = simplejson.load(open(fp))
except: #this needs to be json
    raise


print js
