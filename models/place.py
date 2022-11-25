#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
#from sqlalchemy import Column, String, ForeignKey
#from sqlalchemy.orm import relationship


class Place(BaseModel):
    """ A place to stay """
    city_id ="" 
    user_id = ""
    name = ""
    description = ""
    __tablename__ = 'places'
#    city_id = Column(String(60), nullable=False, ForeignKey="cities.id")
#    user_id = Column(String(60), nullable=False, ForeignKey="users.id")
#    name = Column(String(128), nullable=False)
#    description = Column(String(1024), nullable=True)
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
