#!/usr/bin/env python3
""" Define a new class Square with an attribut size and condition"""


class Square:
    """ Condition declaration for size"""

    def __init__(self, size):
        """ def a private instance"""
        self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")
        if isinstance(size, int):
            raise TypeError("size must be an integer")
