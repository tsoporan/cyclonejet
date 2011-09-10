from datetime import datetime
from cyclonejet import db
from cyclonejet.models import Tag
from cyclonejet.models import User

class Anime(db.Model):
    
    __tablename__ = 'anime'
    
    id = db.Column(db.Integer, primary_key=True)
    
    title = db.Column(db.Unicode(250), unique=True)
    created = db.Column(db.DateTime, default=dateime.utcnow())
    description = db.Column(db.UnicodeText)
    #link is foreignkey
    #genres/tags is m2m
    #

    uploader = db.relation(User)


    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Anime: %r>' % self.title


