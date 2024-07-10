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


class Volunteer(User):
    """ User class definition"""

    __tablename__ = 'volunteers'
    
    id = Column(String(36), ForeignKey('users.id'), primary_key=True)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    gender = Column(String(10), nullable=True)
    date_of_birth = Column(Date, nullable=True)
    phone_number = Column(String(20), nullable=True) 
    location = Column(String(100), nullable=True)
    skills = Column(JSON)
    interests = Column(JSON)
    availability = Column(String(100), nullable=True)
    bio = Column(Text, nullable=True)
    profile_picture_url = Column(String(255), nullable=True)

