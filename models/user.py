#!/usr/bin/python3
"""This is the user class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user
    Attributes:
        email: email address (string, 128 chars, not null)
        password: password for login (string, 128 chars, not null)
        first_name: first name (string, 128 chars, nullable)
        last_name: last name (string, 128 chars, nullable)
        places: relationship with Place objects
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    reviews = relationship('Review', cascade='all, delete', backref='user')
    places = relationship('Place', cascade='all, delete', backref='user')
