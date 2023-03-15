#!/usr/bin/python3
"""base_model"""

from models import storage
from datetime import datetime
import uuid


class BaseModel:
    """ class BaseModel that defines all common attributes/methods
    for other classes
    """

    def __init__(self, *args, **kwargs):
        """BaseModel constructor

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
            if not hasattr(self, 'id'):
                setattr(self, 'id', str(uuid.uuid4()))
            time = datetime.now()
            if not hasattr(self, 'created_at'):
                setattr(self, 'created_at', time)
            if not hasattr(self, 'updated_at'):
                setattr(self, 'updated_at', time)                  
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """string representation"""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
