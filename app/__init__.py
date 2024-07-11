""" creating a flask app"""
from os import getenv, urandom
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
# from models.volunteer import Volunteer
# from models.organization import Organization


db = SQLAlchemy()
mg = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()

VC_MYSQL_USER = getenv('VC_MYSQL_USER')
VC_MYSQL_PWD = getenv('VC_MYSQL_PWD')
VC_MYSQL_HOST = getenv('VC_MYSQL_HOST')
VC_MYSQL_DB = getenv('VC_MYSQL_DB')
# SECRET_KEY = getenv('SECRET_KEY')

database = f'mysql+mysqldb://{VC_MYSQL_USER}:{VC_MYSQL_PWD}@{VC_MYSQL_HOST}/{VC_MYSQL_DB}'


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = urandom(24)

    db.init_app(app)
    mg.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        from .models.user import User
        return User.query.get(str(user_id))

    from .routes import user_routes
    from .routes import volunteer_routes
    from .routes import organization_routes
    from .routes import opportunity_routes
    from .routes import application_routes
    from .routes import auth_routes

    app.register_blueprint(user_routes.bp)
    app.register_blueprint(volunteer_routes.bp)
    app.register_blueprint(organization_routes.bp)
    app.register_blueprint(opportunity_routes.bp)
    app.register_blueprint(application_routes.bp)
    app.register_blueprint(auth_routes.bp)

    return app
