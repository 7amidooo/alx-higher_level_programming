#!/usr/bin/python3
"""
Function to list items of the class
"""


def lookup(obj):
    """
    Lookup(obj)
    Return: List of obj attributes and methods
    """
    obj1 = obj()
    return obj1.__dir__()
