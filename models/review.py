#!/usr/bin/python3
"""
[Review classss]
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    [Review]

    Args:
        BaseModel ([class]): class that inherited by Review
    """
    place_id = ""
    user_id = ""
    text = ""
