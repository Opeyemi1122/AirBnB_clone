#!/usr/bin/python3
"""represents User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents the user.

    Attributes:
    email: email of user
    password: users password
    first_name: first name of the user
    last_name: the last name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

