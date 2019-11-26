import  json
from app import login_manager, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import  send_file
from sqlalchemy.ext import mutable

# @source https://www.michaelcho.me/article/json-field-type-in-sqlalchemy-flask-python

class JsonEncodedDict(db.TypeDecorator):

    impl = db.Text

    def process_bind_param(self, value, dialect):
        if value is None:
            return '{}'
        else:
            return json.dumps(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return {}
        else:
            return json.loads(value)

mutable.MutableDict.associate_with(JsonEncodedDict)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    comment = db.Column(db.String(255))
    group = db.Column(db.String(255), nullable=False)
    start_date = db.Column(db.Date, index=True, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

class Home(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(255))
    banner = db.Column(db.String(255))
    tagline = db.Column(db.Text)
    menu = db.Column(JsonEncodedDict)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()