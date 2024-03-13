#!/usr/bin/python3
"""Defines a State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """represents a state.

    Attributes:
        name (string): name of the state.
    """

    name = ""
