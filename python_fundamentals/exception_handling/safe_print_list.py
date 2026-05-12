#!/usr/bin/env python3
"""Module for safe list printing"""


def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list and returns the real count printed"""
    compteur = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            compteur += 1
        except IndexError:
            if x > compteur:
                break
    print()
    return compteur
