from .base_model import BaseModel
from .. import db


class Application(BaseModel, db.Model):
    """Application class"""
    __tablename__ = 'applications'

    volunteer_id = db.Column(db.String(36), db.ForeignKey('volunteers.id'), nullable=False)
    opportunity_id = db.Column(db.String(36), db.ForeignKey('opportunities.id'), nullable=False)
    status = db.Column(db.String(50), default='Pending')
