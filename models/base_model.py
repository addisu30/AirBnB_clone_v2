#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String

Base = declarative_base()


class BaseModel:
    """A BaseModel class for all hbnb models"""
    
    Attributes:
        id (sqlalchemy DateTime): The datetime at creation.
        created_at (sqlalchemy DateTime): The datetime of last update.
    """
    
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
    
        Args:
            *args (any):- unused.
            **kwargs (dict): key/value pairs of attributes.
        """
        
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    valye = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
    
      def save(self):
        """Updates updated_at with current datetime."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()  
       
    def to_dict(self):
        """Return a dictionaryrepresentation of the BaseModel instance.
        
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict.pop("_sa_instance_state", None)
        return my_dict

    def delete(self):
        """Delete the current instance from storage."""
        models.storage.delete(self)

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        d = self.__dict__.copy()
        d.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)
