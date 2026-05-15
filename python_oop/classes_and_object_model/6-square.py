#!/usr/bin/env python3
""" Define a new class Square with an attribut size and condition"""


class Square():
    """ Condition declaration for size"""

    def __init__(self, size=0, positon=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def __build_string(self):
        result = []  # on crée une liste vide qui va stocker chaque ligne
        if self.__size == 0:
            return "\n"  # si size = 0, on retourne juste une ligne vide

        for _ in range(self.__position[1]):
            result.append("")

        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(result)

    def my_print(self):
        print(self.__build_string)

    def __str__(self):
        print(self.__build_string)

    def area(self):
        return self.__size ** 2  # ** veut dire puissance
