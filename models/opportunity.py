#!/usr/bin/python3
""" User model"""
from models.base_model import BaseModel, Base
from models.user import User
from sqlalchemy import Column, String, ForeignKey, Date, Text, JSON
from sqlalchemy.orm import mapper
import mysql.connector
import uuid
from datetime import datetime
import models


class Opportunity(BaseModel):
    """ Opportunity class definition"""

    __tablename__ = 'opportunities'
    
    org_id = Column(String(36), ForeignKey('organizations.id'), nullable=False)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=False)
    skills_required = Column(JSON)
    interests_required = Column(JSON)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    location = Column(String(255), nullable=False)

