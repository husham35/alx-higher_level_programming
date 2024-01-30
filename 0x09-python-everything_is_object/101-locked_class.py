#!/usr/bin/python3
"""
    Module containing definition of LockedClass class.
"""


class LockedClass:
    """
    LockedClass definition, only allows the
    creation attribute called first_name.
    """
    __slots__ = ["first_name"]
