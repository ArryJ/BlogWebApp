from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '<insert your secret key here>'

# DB Connection

# suppress SQLAlchemy warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# get abs path to the app dir to create the db here
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'blog.db')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from blog import routes