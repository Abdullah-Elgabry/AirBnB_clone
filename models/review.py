#!/usr/bin/python3
"""This module creates a Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """this Class will moderate the rewives"""

    place_id = ""
    user_id = ""
    text = ""
