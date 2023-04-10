#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the State class."""
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Represents a state for a MySQL database.
    Inherits from SQLAlchemy Base and links to the MySQL table states.
    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (sqlalchemy String): The name of the State.
        cities (sqlalchemy relationship): The State-City relationship.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
=======
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base, Column
from models import relationship, String
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", back_populates="state")

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
    else:
        @property
        def cities(self):
            city_list = []
            for city in list(models.storage.all("City").values()):
>>>>>>> 20222ba05ffb64fd4dc0d5bf49800b20d555745d
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
