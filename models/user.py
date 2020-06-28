#!/usr/bin/python3
""" User Model | inherites from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ user class """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
