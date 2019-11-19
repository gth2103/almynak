import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/almynak.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

#Change depending on server
app.config['IMAGE_UPLOADS'] = app.root_path + "/static/images"
app.config['ALLOWED_IMAGE_EXTENSIONS'] = ["PNG", "JPG", "JPEG", "GIF"]

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view == "login"

from app import views, models