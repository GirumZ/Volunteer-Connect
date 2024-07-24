from sqlalchemy import ForeignKey
from .user import User
from .. import db


class Volunteer(User, db.Model):
    """Volunteer class"""
    __tablename__ = 'volunteers'

    id = db.Column(db.String(36), db.ForeignKey('users.id'), primary_key=True)
    first_name = db.Column(db.String(128), nullable=False, index=True)
    last_name = db.Column(db.String(128), nullable=False)
    gender = db.Column(db.String(10), nullable=True)
    date_of_birth = db.Column(db.Date, nullable=True)
    phone_number = db.Column(db.String(20), nullable=True)
    location = db.Column(db.String(100), nullable=True)
    skills = db.Column(db.JSON, nullable=True)
    interests = db.Column(db.JSON, nullable=True)
    availability = db.Column(db.JSON, nullable=True)
    bio = db.Column(db.Text, nullable=True)
    profile_picture_url = db.Column(db.String(255), nullable=True)
