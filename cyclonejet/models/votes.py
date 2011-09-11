from cyclonejet import db

from cyclonejet.models.users import User
from cyclonejet.models.anime import Anime

class Vote(db.Model):

    id = db.Column('id', db.Integer, primary_key=True)
    discriminator = db.Column('type', db.String(50))
    __mapper_args__ = {'polymorphic_on': discriminator}

    score = db.Column('score', db.Integer)

    user_id = db.Column('user_id', db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User, backref='votes')

    def __init__(self, score, user):
        self.score = score
        self.user = user

    def __repr__(self):
        return '<Vote: %r - %r>' % (self.discriminator, self.user.username)

class AnimeVote(Vote):
    __mapper_args__ = {'polymorphic_identity': 'animevote'}

    anime_id = db.Column(db.Integer, db.ForeignKey(Anime.id))
    anime = db.relationship(Anime, backref='votes')

    def __init__(self, score, user, anime):
        super(AnimeVote, self).__init__(score, user)
        self.anime = anime

