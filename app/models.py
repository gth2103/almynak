import  json
from app import login_manager, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import  send_file
from sqlalchemy.ext import mutable

# @source https://www.michaelcho.me/article/json-field-type-in-sqlalchemy-flask-python

#db.drop_all()

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
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    users = db.relationship('User', backref='group', lazy=True, cascade="all, delete")
    homepages = db.relationship('Home', backref='group', lazy=True, cascade="all, delete")
    base_configs = db.relationship('BaseConfig', backref='group', lazy=True, cascade="all, delete")
    members = db.relationship('Member', backref='group', lazy=True, cascade="all, delete")

class Home(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    background = db.Column(db.String(255), nullable=False)
    banner = db.Column(db.String(255), nullable=False)
    tagline = db.Column(db.Text, nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    founder = db.Column(db.Boolean)
    name = db.Column(db.String(120), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    about = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    coffee = db.Column(db.String(120), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)

class BaseConfig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(255), nullable=False)
    menu = db.Column(JsonEncodedDict, nullable=False)
    color = db.Column(db.String(10), nullable=False)
    facebook = db.Column(db.String(120), nullable=False)
    twitter = db.Column(db.String(120), nullable=False)
    instagram = db.Column(db.String(120), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()