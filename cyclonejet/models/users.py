from cyclonejet import db
import datetime

from werkzeug import generate_password_hash, check_password_hash

groups = db.Table('groups', 
        db.Column('group_id', db.Integer, db.ForeignKey('group.id')),
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
)

class User(db.Model):
    # A user.

    id = db.Column(db.Integer, primary_key=True)
    
    username = db.Column(db.Unicode(60), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150))

    groups = db.relationship('Group', secondary=groups, backref=db.backref('users'))

    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    profile = db.relationship('Profile', uselist=False, backref='user')

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        if password:
            return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User: %r>' % self.username


class Profile(db.Model):
    # A user has a profile
    
    id = db.Column(db.Integer, primary_key=True)
   
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    reputation = db.Column(db.Integer)
    gravatar = db.Column(db.String(250)) #gravatar url

    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Profile: %r>' % self.user


class Group(db.Model):
    # A user can belong to multiple groups.
    
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.Unicode(250), unique=True, nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<UserGroup: %r>' % self.name
