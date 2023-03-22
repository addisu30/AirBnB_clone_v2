#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime
<<<<<<< HEAD
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime
=======
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String
>>>>>>> 16245d8589ac45353f7b35bea2571d2ed8c3810b

Base = declarative_base()


class BaseModel:
<<<<<<< HEAD
    """A base class for all hbnb models"""
    id = Column("id", String(60), primary_key=True, nullable=False)
    created_at = Column("created_at", DateTime, nullable=False,
                        default=datetime.utcnow())
    updated_at = Column("updated_at", DateTime, nullable=False,
                        default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary if dictionary.get("_sa_instance_state") is None\
            else dictionary.__delitem__("_sa_instance_state")

    def delete(self):
        """delete the current instance from the database storage"""
        from models import storage
        storage.delete(self)
=======
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
>>>>>>> 16245d8589ac45353f7b35bea2571d2ed8c3810b
