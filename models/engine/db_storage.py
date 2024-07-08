#!/usr/bin/python3
""" Database storage"""
from os import getenv
import models
from models.base_model import BaseModel, Base
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """ DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        VC_MYSQL_USER = getenv('VC_MYSQL_USER')
        VC_MYSQL_PWD = getenv('VC_MYSQL_PWD')
        VC_MYSQL_HOST = getenv('VC_MYSQL_HOST') 
        VC_MYSQL_DB = getenv('VC_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                       format(VC_MYSQL_USER,
                                              VC_MYSQL_PWD,
                                              VC_MYSQL_HOST,
                                              VC_MYSQL_DB))

    def new(self, obj):
        """ Adds new object to the database"""
        self.__session.add(obj)

    def save(self):
        """ Saves currunt session data to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes an object from the database"""
        self.__session.delete(obj)

    def reload(self):
        """ Reloads data from the database"""

        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session
    
    def close(self):
        """ Removes any object from the session"""
        self.__session.remove()

    def get(self, cls, id):
        """ Returns a specific instance of a class using the id attribute"""

        if cls and id:
            all_objs = models.storage.all(cls)
            for value in all_objs.values():
                if (value.id == id):
                    return value
        return None

    def conunt(self, cls=None):
        """ Conunts the numbers of instances of a class"""

        return(len(self.all(cls)))
