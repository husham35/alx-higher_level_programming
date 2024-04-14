#!/usr/bin/python3
"""
Module definitoin of a `City` class with link to the MySQL table `cities`
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """
    City class definition with its attributes.

    Attributes:
        id (int): The primary key for the table.
        name (str): The name of the city.
    """

    __tablename__ = 'cities'

    id: int = Column(Integer, primary_key=True)
    name: int = Column(String(128), nullable=False)
    state_id: int = Column(Integer, ForeignKey('states.id'))

    state = relationship('State', backref='cities')
