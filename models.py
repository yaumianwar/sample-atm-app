from db import database

class User(database.Model):
	__tablename__ = 'user'

	id = database.Column(database.Integer, primary_key = True)
	full_name = database.Column(database.String(120))
	email = database.Column(database.String(64), unique = True)
	password = database.Column(database.String(255))
	bio = database.Column(database.String(70))
	avatar = database.Column(database.String(11))
    posts = db.relationship('Post', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')
    likes = db.relationship('Like', backref='user', lazy='dynamic')
	registered = database.Column(database.DateTime)
	last_login = database.Column(database.DateTime)

	def __init__(self, full_name, email, password, bio,
				avatar):
		self.full_name = full_name
		self.email = email
		self.password = password
		self.bio = bio
		self.avatar = avatar

	def __repr__(self):
		return 'User {}>'.format(self.full_name)

class Post(database.Model):
    __tablename__ = 'post'

    id = database.Column(database.Integer, primary_key = True)
    title = database.Column(database.String(50))
    content = database.Column(database.String(200))
    id_user= database.Column(database.Integer,
                             database.ForeignKey('user.id'))
    comments = db.relationship('Comment', backref='user', lazy='dynamic')
    likes = db.relationship('Like', backref='user', lazy='dynamic')
    createdtime = database.Column(database.DateTime)
    updatedtime = database.Column(database.DateTime)
    deletedtime = database.Column(database.DateTime)
    deleted = database.Column(database.Integer)

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return 'Post {}>'.format(self.title)

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
        return 'Comment {}>'.format(self.desc)

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
