# -------------------------------------------------------------#
#   Here we initialise the project & basic setup               #
# -------------------------------------------------------------#
import sqlalchemy
from flask import Flask
import os
import flask_migrate
from sqlalchemy_utils import database_exists, create_database

from flask_sqlalchemy import SQLAlchemy

template_dir = os.path.abspath('templates/')
static_dir = os.path.abspath('static/')
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# -------------------------------------------------------------#
#   Database Setup with SQLAlchemy as ORM                      #
# -------------------------------------------------------------#
db = SQLAlchemy()

user = os.environ.get('POSTGRES_USER', 'postgres')
password = os.environ.get('POSTGRES_PASSWORD', 'postgres')
host = os.environ.get('POSTGRES_HOST', 'localhost')
database = os.environ.get('POSTGRES_DB', 'db')
port = os.environ.get('POSTGRES_PORT', 5432)

DATABASE_CONNECTION_URI = f'postgresql://{user}:{password}@{host}:{port}/{database}'

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
engine = sqlalchemy.create_engine(DATABASE_CONNECTION_URI, echo=True)

if database_exists(DATABASE_CONNECTION_URI):
    print('DB Exists')
else:
    create_database(DATABASE_CONNECTION_URI)
    print('DB does not exist')

session = engine.connect()
db.init_app(app)

# Migrate / Migrations
migrate = flask_migrate.Migrate()
migrate.init_app(app, db)

app.secret_key = 'test'
import controllers
import api

import error_handlers
from models.superheros import Superheros