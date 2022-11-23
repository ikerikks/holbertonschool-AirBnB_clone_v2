#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Foreignkey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Colunm(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, foreign_key=True)
    places = relationship("Place", backref="cities", cascade="all, delete")
