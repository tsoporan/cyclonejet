import datetime
from cyclonejet.extensions import db
from cyclonejet.models.users import User

class Anime(db.Model):
    
    __tablename__ = 'anime'
    
    id = db.Column(db.Integer, primary_key=True)
    
    title = db.Column(db.Unicode(250), unique=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    description = db.Column(db.UnicodeText)
   
    #genres ?
    #type? (series,ova,movie)

    uploader_id = db.Column(db.Integer, db.ForeignKey(User.id))
    uploader = db.relationship(User, backref='animes')

    def __init__(self, title, description=None):
        self.title = title
        if description:
            self.description = description

    def __repr__(self):
        return '<Anime: %r>' % self.title

#class Episode(db.Model):
# many episodes -> one anime

