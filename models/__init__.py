#!/usr/bin/python3
<<<<<<< HEAD
"""Instantiates a storage object.
-> If the environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
   instantiates a database storage engine (DBStorage).
-> Otherwise, instantiates a file storage engine (FileStorage).
"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
=======
"""This module instantiates an object of class FileStorage"""
import os
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, String


if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from .engine import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from .engine import FileStorage
    storage = FileStorage()
    storage.reload()
>>>>>>> 20222ba05ffb64fd4dc0d5bf49800b20d555745d
