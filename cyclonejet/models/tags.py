import datetime
from cyclonejet import db

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Tag: %r>' % self.name
