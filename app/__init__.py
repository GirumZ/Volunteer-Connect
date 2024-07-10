""" creating a flask app"""
from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
mg = Migrate()

VC_MYSQL_USER = getenv('VC_MYSQL_USER')
VC_MYSQL_PWD = getenv('VC_MYSQL_PWD')
VC_MYSQL_HOST = getenv('VC_MYSQL_HOST')
VC_MYSQL_DB = getenv('VC_MYSQL_DB')

database = f'mysql+mysqldb://{VC_MYSQL_USER}:{VC_MYSQL_PWD}@{VC_MYSQL_HOST}/{VC_MYSQL_DB}'


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    mg.init_app(app, db)

    from .routes import user_routes

    app.register_blueprint(user_routes.bp)

    return app
