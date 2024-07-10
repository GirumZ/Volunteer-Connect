from .base_model import BaseModel
from .. import db


class User(BaseModel, db.Model):
    """ User class definition"""

    __tablename__ = 'users'

    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
