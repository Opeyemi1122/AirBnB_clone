#!/usr/bin/python3
"""defines the BaseModel class."""
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """represents the BaseModel of the AirBnB project."""

    def __init__(self, *args, **kwargs):
        """initializes the new BaseModel

        Args:
            *args (any): Unused.
            **kwargs (dictoionary): Key/calue pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, v in kwargs.items():
                if key == "created at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(v, tform)
                else:
                    self.__dict__[key] = v
        else:
            models.storage.new(self)
