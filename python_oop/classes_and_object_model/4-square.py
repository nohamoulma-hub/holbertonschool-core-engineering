#!/usr/bin/env python3
""" Define a new class Square with an attribut size and condition"""


class Square():
    """ Condition declaration for size"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return self.__size ** 2  # ** veut dire puissance
