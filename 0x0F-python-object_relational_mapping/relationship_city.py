#!/usr/bin/python3
"""
Module definition for a `City` class that represents a table `cities`
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """
    City class definition for a cities table in a database

    Attributes:
        id (int): The primary key for the table.
        name (str): The name of the city.
        state_id (int): The id of the state in the state table.
    """

    __tablename__ = 'cities'

    id: int = Column(Integer, primary_key=True)
    name: int = Column(String(128), nullable=False)
    state_id: int = Column(Integer, ForeignKey('states.id'))
