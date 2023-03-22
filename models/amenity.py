#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel
from sqlalchemy import Column, String


class Amenity(BaseModel):
    """Amenities to purchase from the site"""

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"

        name = Column("name", String(128), nullable=False)
