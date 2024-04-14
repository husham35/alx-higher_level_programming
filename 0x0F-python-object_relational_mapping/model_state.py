#!/usr/bin/python3
"""
Module definitoin of a `State` class with link to the MySQL table `states`
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class definition with its attributes.

    Attributes:
        id (int): primary key for states table.
        name (str): name of state.
    """

    __tablename__ = 'states'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
