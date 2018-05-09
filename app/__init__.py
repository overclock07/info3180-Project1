from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"

POSTGRES = {
    'user': 'postgres',
    'pw': 'password',
    'db': 'project1',
    'host': '0.0.0.0',
    'port': '5432',
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://nfajwkhxbdktgd:282fbb1ce7872970eaba2384a70573e02d962d98bc8860bc3ce896bc6602081b@ec2-23-23-248-192.compute-1.amazonaws.com:5432/dboa7061d50rtl'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
#%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

#UPLOAD_FOLDER = "./app/static/uploads"
# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

UPLOAD_FOLDER = 'app/static/img/'

app.config.from_object(__name__)
from app import views
