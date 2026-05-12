#!/usr/bin/env python3
""" Module for safe print integer """


def safe_print_integer(value):
    """ Print value if is an integer """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
