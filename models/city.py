#!/usr/bin/python3
""" City Module for HBNB project """
<<<<<<< HEAD
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
=======
import os
from models.base_model import Base
from models.base_model import Column, Integer, BaseModel
from models import relationship, String
from sqlalchemy import ForeignKey
>>>>>>> 20222ba05ffb64fd4dc0d5bf49800b20d555745d


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
<<<<<<< HEAD
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", backref="cities", cascade="all, delete")
=======
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        state = relationship("State", back_populates="cities")
        places = relationship("Place", back_populates="cities")
>>>>>>> 20222ba05ffb64fd4dc0d5bf49800b20d555745d
