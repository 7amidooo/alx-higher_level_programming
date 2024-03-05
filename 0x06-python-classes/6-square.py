#!/usr/bin/python3

"""New class"""


class Square:
    """Square"""

    def __init__(self, sz=0, position=(0, 0)):
        if sz.__class__ != int:
            raise TypeError("size must be an integer")
        elif sz < 0:
            raise ValueError("size must be >= 0")
        self.__size = sz
        if position.__class__ != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):

        return self.__size * self.__size

    @property
    def size(self):

        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if value.__class__ != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):
        if value.__class__ != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()

        for i in range(0, self.__size):
            for k in range(0, self.__position[0]):
                print("_", end='')
            for j in range(0, self.__size):
                print('#', end='')
            print()
