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


class Organization(User):
    """ Organization class definition"""

    __tablename__ = 'organizations'
    
    id = Column(String(36), ForeignKey('users.id'), primary_key=True)
    org_name = Column(String(128), nullable=False)
    est_date = Column(Date, nullable=True)
    mission_statement = Column(Text, nullable=True)
    contact_email = Column(String(100), nullable=True)
    contact_phone = Column(String(20), nullable=True) 
    location = Column(String(100), nullable=True)
    website_url = Column(String(255), nullable=True)
    profile_picture_url = Column(String(255), nullable=True)

