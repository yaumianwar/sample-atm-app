from app.core.db import database
from app.user.models import User
from slugify import slugify
from unicodedata import normalize

class Transfer(database.Model):
    __tablename__ = 'transfer'

    id = database.Column(database.Integer, primary_key = True)
    value = database.Column(database.Integer)
    tujuan = database.Column(database.Integer)
    id_user= database.Column(database.Integer,
                             database.ForeignKey('user.id'))
    createdtime = database.Column(database.DateTime)
    updatedtime = database.Column(database.DateTime)
    deletedtime = database.Column(database.DateTime)
    deleted = database.Column(database.Integer)

    def __init__(self, value, tujuan, id_user):
        self.value = value
        self.tujuan = tujuan
        self.id_user = id_user

    def __repr__(self):
        return '<Transfer {}>'.format(self.value)

class Penarikan(database.Model):
    __tablename__ = 'penarikan'

    id = database.Column(database.Integer, primary_key = True)
    value = database.Column(database.Integer)
    id_user= database.Column(database.Integer,
                             database.ForeignKey('user.id'))
    createdtime = database.Column(database.DateTime)
    updatedtime = database.Column(database.DateTime)
    deletedtime = database.Column(database.DateTime)
    deleted = database.Column(database.Integer)

    def __init__(self, value, id_user):
        self.value = value
        self.id_user = id_user

    def __repr__(self):
        return '<Penarikan {}>'.format(self.value)

class Pemasukan(database.Model):
    __tablename__ = 'pemasukan'

    id = database.Column(database.Integer, primary_key = True)
    value = database.Column(database.Integer)
    id_user= database.Column(database.Integer,
                             database.ForeignKey('user.id'))
    createdtime = database.Column(database.DateTime)
    updatedtime = database.Column(database.DateTime)
    deletedtime = database.Column(database.DateTime)
    deleted = database.Column(database.Integer)

    def __init__(self, value, id_user):
        self.value = value
        self.id_user = id_user

    def __repr__(self):
        return '<Pemasukan {}>'.format(self.value)
