from flask_login import UserMixin
from .base_model import BaseModel
from app import db
from app import bcrypt


class User(UserMixin, BaseModel, db.Model):
    """ User class definition"""

    __tablename__ = 'users'

    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    def check_password(self, password):
        return bycrypt.check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.id
