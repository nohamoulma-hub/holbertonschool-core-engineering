#!/usr/bin/env python3
""" Define a new class Square with an attribut size and condition"""


class Square():
    """ Condition declaration for size"""

    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
    
    def area(self):
        return self.__size ** 2  # ** veut dire puissance 
