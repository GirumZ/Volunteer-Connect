#!/usr/bin/python3
""" User model"""
from models.base_model import BaseModel, Base
from models.user import User
from sqlalchemy import Column, String, ForeignKey, Date, Text
from sqlalchemy.orm import mapper
import mysql.connector
import uuid
from datetime import datetime
import models


class Application(BaseModel):
    """ Application class definition"""

    __tablename__ = 'applications'
    
    volunteer_id = Column(String(36), ForeignKey('volunteers.id'), nullable=False)
    opportunity_id = Column(String(36), ForeignKey('opportunities.id'), nullable=False)
    status = Column(String(50), default='Pending')
