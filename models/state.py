#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
#from sqlalchemy import Column, String
#from sqlalchemy.orm import relationship
#from os import getenv
#from models.city import City

class State(BaseModel):
    """ State class """
#    __tablename__ = 'states'
#    name = Column(String(128), nullable=False)
#    cities = relationship("City", back_populates="state",
#                          cascade="all, delete")

#    if getenv('HBNB_TYPE_STORAGE') == 'db':
#        @property
#        def cities(self):
#            """Getter of cities"""
#            from models import storage
            # from models.city import City
#            list_city = []
#            for city in storage.all(City):
#                if self.id == city.state_id:
#                    list_city.append(city)
#            return list_city 
    name = ""
