#!/usr/bin/python3

"""New class"""


class Square:
    """Square"""
    def __init__(self, sz=0):
        if sz.__class__ != int:
            raise TypeError("size must be an integer")
        elif sz < 0:
            raise ValueError("size must be >= 0")
        self.__size = sz
