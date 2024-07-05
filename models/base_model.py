#!/usr/bin/python3
""" BaseModel"""
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
import mysql.connector
import uuid
from datetime import datetime
import models


time = '%Y-%m-%dT%H:%M:%S.%f'
Base = declarative_base()

class BaseModel(Base):

    __tablename__ = 'BaseModel'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        """ String representatin of the BaseModel instances"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Saves an instance to the database"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary that contains all key/values of an instance"""

        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]

        return new_dict

    def delete(self):
        """ Deletes the current instance from the database"""
        models.storage.delete(self)        
