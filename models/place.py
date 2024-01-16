#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from os import environ
from sqlalchemy.orm import relationship


class Place(BaseModel):
    """ A place to stay """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    if environ['HBNB_TYPE_STORAGE'] == 'db':
        reviews = relationship('Review', cascade='all, delete', backref='place')
    else:
        @property
        def reviews(self):
            """
            getter method that
            returns the list of Review instances with place_id
            equals to the current Place.id
            """
            from models import storage
            from models.review import Review
            # get the dict of all the reviews
            review_dict = storage.all()
            review_list = []
            # loop though the reviews, map those that correspond to current
            # place_id
            for review in review_dict.values():
                if Review.place_id == self.id:
                    review_list.append(review)
            # return list of corressponding reviews
            return review_list
 
