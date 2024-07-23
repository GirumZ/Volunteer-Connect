from .base_model import BaseModel
from .. import db


class Opportunity(BaseModel, db.Model):
    """Opportunity class"""
    __tablename__ = 'opportunities'

    org_id = db.Column(db.String(36), db.ForeignKey('organizations.id'), nullable=False)
    org_name = db.Column(db.String(128), db.ForeignKey('organizations.org_name'), nullable=False) 
    title = db.Column(db.String(150), nullable=False, index=True)
    opp_type = db.Column(db.String(10), default="On site", index=True)
    description = db.Column(db.String(255), nullable=False, index=True)
    skills_required = db.Column(db.JSON, nullable=False)
    interests_required = db.Column(db.JSON, nullable=False)
    start_date = db.Column(db.Date, nullable=False, index=True)
    end_date = db.Column(db.Date, nullable=True, index=True)
    contact_email = db.Column(db.String(100), db.ForeignKey('organizations.contact_email'))
    contact_phone = db.Column(db.String(20), db.ForeignKey('organizations.contact_phone'))
    location = db.Column(db.String(255), nullable=False, index=True)
