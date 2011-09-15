import datetime
from cyclonejet.extensions import db
from werkzeug import generate_password_hash, check_password_hash

from flaskext.sqlalchemy import BaseQuery

groups = db.Table('groups', 
        db.Column('group_id', db.Integer, db.ForeignKey('group.id')),
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
)

class UserQuery(BaseQuery):

    @staticmethod
    def create_user(username, email, password, admin=False):
        if admin:
            user = User.query.filter_by(role=User.ADMIN).first()
        else:
            user = User.query.filter_by(username=username).first()
        
        if not user:
            user = User(username, email, password)
            if admin:
                user.role = User.ADMIN
            db.session.add(user)
            db.session.commit()
        return user


class User(db.Model):
    # A user.

    MEMBER = 1
    ADMIN = 2

    query_class = UserQuery

    id = db.Column(db.Integer, primary_key=True)
    
    username = db.Column(db.Unicode(60), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150))

    groups = db.relationship('Group', secondary=groups, backref=db.backref('users'))

    role = db.Column(db.Integer, default=MEMBER)

    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    profile = db.relationship('Profile', uselist=False, backref='user')

    is_verified = db.Column(db.Boolean, default=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)


    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        if password:
            return check_password_hash(self.password, password)

    def change_password(self, new_password, old_password=None):
        if old_password:
            if not self.check_password(old_password): 
                return False

        self.set_password(new_password)

    def send_mail(self, subject, message, from_email=False):
        pass

    def join_group(self, group):
        self.groups.append(group)

    def leave_group(self, group):
        self.groups.remove(group)

    def is_admin(self):
        if self.role == 2:
            return True

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
