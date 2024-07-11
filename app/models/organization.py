from .user import User
from .. import db


class Organization(User, db.Model):
    """ Organization class"""
    __tablename__ = 'organizations'

    id = db.Column(db.String(36), db.ForeignKey('users.id'), primary_key=True)
    org_name = db.Column(db.String(128), nullable=False)
    est_date = db.Column(db.Date, nullable=True)
    mission_statement = db.Column(db.Text, nullable=True)
    contact_email = db.Column(db.String(100), nullable=True)
    contact_phone = db.Column(db.String(20), nullable=True)
    location = db.Column(db.String(100), nullable=True)
    website_url = db.Column(db.String(255), nullable=True)
    profile_picture_url = db.Column(db.String(255), nullable=True)
