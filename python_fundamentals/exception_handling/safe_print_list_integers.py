#!/usr/bin/env python3
""" Module for safe print list integer """


def safe_print_list_integers(my_list=[], x=0):
    """Prints x elements integer of a list and
    returns the real count printed"""

    compteur = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            compteur += 1
        except ValueError:
            continue
        except TypeError:
            continue
        except IndexError:
            print()
            return compteur
    print()
    return compteur
