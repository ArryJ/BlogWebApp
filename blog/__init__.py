from flask import Flask
# import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'cbbe1aaa03a204bf62887b20d70a2ed33c499e9422ec5505'

# DB Connection

# suppress SQLAlchemy warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# get abs path to the app dir to create the db here
# basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c21045550:mySQLpass123@csmysql.cs.cf.ac.uk:3306/c21045550_blog_db'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from blog import routes
