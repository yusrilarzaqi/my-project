from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '559e63b9ae803b889d8737df'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from . import routes
