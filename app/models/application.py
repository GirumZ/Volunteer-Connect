from .base_model import BaseModel
from .. import db


class Application(BaseModel, db.Model):
    """Application class"""
    __tablename__ = 'applications'

    volunteer_id = db.Column(db.String(36), db.ForeignKey('volunteers.id'), nullable=False)
    opportunity_id = db.Column(db.String(36), db.ForeignKey('opportunities.id'), nullable=False)
    org_id = db.Column(db.String(36), db.ForeignKey('opportunities.org_id'))
    org_name = db.Column(db.String(128), db.ForeignKey('opportunities.org_name'))
    opp_title = db.Column(db.String(150), db.ForeignKey('opportunities.title'))
    opp_description = db.Column(db.String(255), db.ForeignKey('opportunities.description'))
    opp_start_date = db.Column(db.Date, db.ForeignKey('opportunities.start_date'))
    opp_end_date = db.Column(db.Date, db.ForeignKey('opportunities.end_date'))
    opp_start_date = db.Column(db.Date, db.ForeignKey('opportunities.start_date'))
    contact_email = db.Column(db.String(100), db.ForeignKey('opportunities.contact_email'))
    contact_phone = db.Column(db.String(20), db.ForeignKey('opportunities.contact_phone'))
    location = db.Column(db.String(255), db.ForeignKey('opportunities.location'))



    status = db.Column(db.String(50), default='Pending')
