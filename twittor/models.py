from datetime import datetime
from twittor import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    tweets = db.relationship('Tweet', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'id={self.id}, username={self.username}, password={self.password_hash}' 

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'id={self.id}, body={self.body}, create_time={self.create_time}, user_id={self.user_id}'

