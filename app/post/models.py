from app.core.db import database
from app.user.models import User
from slugify import slugify

class Post(database.Model):
    __tablename__ = 'post'

    id = database.Column(database.Integer, primary_key = True)
    title = database.Column(database.String(50))
    content = database.Column(database.String(200))
    slug = database.Column(database.String(70), unique = True)
    id_user= database.Column(database.Integer,
                             database.ForeignKey('user.id'))
    comments = database.relationship('Comment', backref='post', lazy='dynamic')
    likes = database.relationship('Like', backref='post', lazy='dynamic')
    createdtime = database.Column(database.DateTime)
    updatedtime = database.Column(database.DateTime)
    deletedtime = database.Column(database.DateTime)
    deleted = database.Column(database.Integer)

    def __init__(self, title, content, id_user):
        self.title = title
        self.content = content
        self.slug = slugify(title)
        self.id_user = id_user

    def __repr__(self):
        return '<Post {}>'.format(self.title)

class Comment(database.Model):
    __tablename__ = 'comment'

    id = database.Column(database.Integer, primary_key = True)
    desc = database.Column(database.String(200))
    id_user= database.Column(database.Integer,
                             database.ForeignKey('user.id'))
    id_post= database.Column(database.Integer,
                             database.ForeignKey('post.id'))
    createdtime = database.Column(database.DateTime)
    updatedtime = database.Column(database.DateTime)
    deletedtime = database.Column(database.DateTime)
    deleted = database.Column(database.Integer)

    def __init__(self, desc):
        self.desc = desc

    def __repr__(self):
        return '<Comment {}>'.format(self.desc)

class Like(database.Model):
    __tablename__ = 'like'

    id = database.Column(database.Integer, primary_key = True)
    id_user= database.Column(database.Integer,
                             database.ForeignKey('user.id'))
    id_post= database.Column(database.Integer,
                             database.ForeignKey('post.id'))
    createdtime = database.Column(database.DateTime)
    updatedtime = database.Column(database.DateTime)
    deletedtime = database.Column(database.DateTime)
    deleted = database.Column(database.Integer)

    def __init__(self, id_user, id_post):
        self.id_user = id_user
        self.id_post = id_post
