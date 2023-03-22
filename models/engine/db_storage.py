#!/usr/bin/python3
"""Thsis file define a class for manage database storage"""
from models.base_model import Base


class DBStorage:
    """class for database storage engine"""
    from models.base_model import BaseModel
    from models.city import City
    from models.place import Place
    from models.state import State
    from models.review import Review
    from models.user import User

    __engine = None
    __session = None
    obj = {"BaseModel": BaseModel, "City": City, "Place": Place,
           "State": State, "Review": Review, "User": User}

    def __init__(self):
        """create the engine that link to the database server"""
        import os
        from sqlalchemy import create_engine

        self.__engine = create_engine("mysql+mysqldb://%s:%s@%s:3306/%s" % (
            os.getenv("HBNB_MYSQL_USER"),
            os.getenv("HBNB_MYSQL_PWD"),
            os.getenv("HBNB_MYSQL_HOST"),
            os.getenv("HBNB_MYSQL_DB")), pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query cls entities in the database base on the cls argument"""
        return_obj = {}
        if cls:
            for entity in self.__session.query(self.obj[cls]).all():
                key = str(entity.__class__.__name__) + "." + entity.id
                return_obj.update({key: entity})
            return return_obj
        else:
            for cls_obj in self.obj:
                for entity in self.__session.query(self.obj[cls_obj]).all():
                    key = str(entity.__class__) + "." + entity.id
                    return_obj.update({key: entity})
            return return_obj

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all chnages from the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session if obj is not None"""
        if obj is not None:
            self.__session.delete(self)

    def reload(self):
        """create all ORM data to the database base on the Base object"""
        from sqlalchemy.orm import sessionmaker, scoped_session

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
