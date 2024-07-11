from .base_model import BaseModel
from .. import db


class Opportunity(BaseModel, db.Model):
    """Opportunity class"""
    __tablename__ = 'opportunities'

    org_id = db.Column(db.String(36), db.ForeignKey('organizations.id'), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    skills_required = db.Column(db.JSON, nullable=False)
    interests_required = db.Column(db.JSON, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)
    location = db.Column(db.String(255), nullable=False)
