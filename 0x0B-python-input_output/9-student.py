#!/usr/bin/python3
"""
Module that defines a student class
"""


class Student:
    """ Student class """

    def __init__(self, first_name, last_name, age):
        """ Initializer """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns a dictionary representation of a student object """
        return self.__dict__
