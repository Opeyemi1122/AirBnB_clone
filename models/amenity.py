#!/usr/bin/python3
"""Defines the amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.

    Attributes:
        name (str): is the name of the amenity.
    """

    name = ""
