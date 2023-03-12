#!/usr/bin/python3
"""
convert the dictionary representation to a JSON string
"""
import json


class FileStorage:
    """a representation of the file storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary of all objects stored
        in the file(file.json) as key,
        value pairs.
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Saves to the file storage, updated models (objects)."""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def classes(self):
        from models.base_model import BaseModel
        classes = {
            'BaseModel': BaseModel,
        }
        return classes

    def reload(self):
        """Loads objects from file storage"""
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                FileStorage.__objects = json.load(f)
                for key, value in FileStorage.__objects.items():
                    cls_name = value['__class__']
                    cls = self.classes()[cls_name]
                    FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
