#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage_type

class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'
    #__table_args__ = ({'mysql_default_charset': 'latin1'})

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship('Place', back_populates='user', cascade='all, delete, save-update')
    reviews = relationship('Review', back_populates='user', cascade='all, delete, save-update')