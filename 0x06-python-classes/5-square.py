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

    def area(self):

        return self.__size * self.__size

    @property
    def size(self):

        return self.__size

    @size.setter
    def size(self, value):
        if value.__class__ != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print('#', end='')
            print()