import datetime
from cyclonejet.extensions import db
from cyclonejet.models.users import User

class Manga(db.Model):

    __tablename__ = 'manga'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.Unicode(250), unique=True, nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    description = db.Column(db.UnicodeText)

    year = db.Column(db.String(10))
    author = db.Column(db.Unicode(250))

    uploader_id = db.Column(db.Integer, db.ForeignKey(User.id))
    uploader = db.relationship(User, backref='mangas')

    def __init__(self, title, description=None, year=None, author=None):
        self.title = title
        self.description = description
        self.year = year
        self.author = author

    def __repr__(self):
        return '<Manga: %r>' % self.title

#class Chapter(db.Model):
#    
#    many chapters -> one manga

