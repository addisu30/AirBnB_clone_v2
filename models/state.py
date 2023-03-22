#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column("name", String(128), nullable=False)

        cities = relationship(City, backref="state")
