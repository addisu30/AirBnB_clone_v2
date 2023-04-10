#!/usr/bin/python3
'''
    This module defines the BaseModel class
'''
import uuid
import models
from datetime import datetime
<<<<<<< HEAD
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

=======
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
>>>>>>> 20222ba05ffb64fd4dc0d5bf49800b20d555745d
Base = declarative_base()


class BaseModel:
<<<<<<< HEAD
    '''
        Base class for other classes to be used for the duration.
    '''
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        '''
            Initialize public instance attributes.
        '''
        if len(kwargs) == 0:
            # if no dictionary of attributes is passed in
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            # assign a dictionary of attributes to instance

            # preserve existing created_at time
            if kwargs.get('created_at'):
                kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.created_at = datetime.utcnow()  # assign current time
            if kwargs.get('updated_at'):
                # preserve existing updated_at time
                kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.updated_at = datetime.utcnow()

            if not kwargs.get('id'):
                self.id = str(uuid.uuid4())

            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        '''
            Return string representation of BaseModel class
        '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        '''
            Return string representation of BaseModel class
        '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        '''
            Update the updated_at attribute with new.
        '''
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        '''
            Return dictionary representation of BaseModel class.
        '''
        cp_dct = dict(self.__dict__)
        cp_dct['__class__'] = self.__class__.__name__
        cp_dct['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        cp_dct['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        if '_sa_instance_state' in cp_dct:
            del cp_dct['_sa_instance_state']
        return cp_dct

    def delete(self):
=======
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False, unique=True)
    created_at = Column(DateTime(), nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime(), nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            for key, value in kwargs.items():
                if key == 'updated_at':
                    kwargs['updated_at'] = \
                            datetime.strptime(kwargs['updated_at'],
                                              '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'created_at':
                    kwargs['created_at'] = \
                            datetime.strptime(kwargs['created_at'],
                                              '%Y-%m-%dT%H:%M:%S.%f')
                elif key != '__class__':
                    setattr(self, key, value)
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        copy_dict = self.__dict__.copy()
        if "_sa_instance_state" in copy_dict:
            del copy_dict["_sa_instance_state"]
        return '[{}] ({}) {}'.format(cls, self.id, copy_dict)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        models.storage.new(self)
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' not in dictionary:
            return dictionary
        else:
            del dictionary['_sa_instance_state']
            return dictionary

    def delete(self):
        """delete current instance from the storage by calling\
                the delete method"""
>>>>>>> 20222ba05ffb64fd4dc0d5bf49800b20d555745d
        models.storage.delete(self)
