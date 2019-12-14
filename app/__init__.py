import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/almynak.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

#Change depending on server
app.config['IMAGE_UPLOADS_FULL'] = app.root_path + "/static/images"
app.config['IMAGE_UPLOADS_REL'] = "/static/images"
app.config['ALLOWED_IMAGE_EXTENSIONS'] = ["PNG", "JPG", "JPEG", "GIF"]

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view == "login"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'gth2103@columbia.edu'
app.config['MAIL_PASSWORD'] = 'SMJ*CV#s'

mail = Mail(app)

from data.seed import *
from app import views, models