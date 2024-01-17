#!/usr/bin/python3
"""This is the city class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """This class defines city
    Attributes:
        state_id: state id (string, 60 chars, not null, foreign key to states.id)
        name: name (string, 128 chars, not null)
        places: relationship with Place objects
    """
    __tablename__ = 'cities'

    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    # Relationship with Place objects
    places = relationship('Place', backref='city', cascade='all, delete-orphan')
