from app.core.db import database


class User(database.Model):
    __tablename__ = 'user'

    id = database.Column(database.Integer, primary_key = True)
    norek = database.Column(database.Integer)
    password = database.Column(database.String(255))
    saldo = database.Column(database.Integer)
    avatar = database.Column(database.String(11))
    transfer = database.relationship('Transfer', backref='user', lazy='dynamic')
    penarikan = database.relationship('Penarikan', backref='user', lazy='dynamic')
    pemasukan = database.relationship('Pemasukan', backref='user', lazy='dynamic')
    registered = database.Column(database.DateTime)
    last_login = database.Column(database.DateTime)

    def __init__(self, norek, password, saldo, avatar):
        self.norek = norek
        self.password = password
        self.saldo = saldo
        self.avatar = avatar

    def __repr__(self):
        return '<User {}>'.format(self.norek)
