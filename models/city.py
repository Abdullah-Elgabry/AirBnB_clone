#!/usr/bin/python3
"""This module creates a User class"""

from models.base_model import BaseModel


class City(BaseModel):
    """this class will moderate the cites"""

    state_id = ""
    name = ""
