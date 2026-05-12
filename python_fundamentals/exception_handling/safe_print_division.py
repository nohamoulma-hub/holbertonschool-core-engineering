#!/usr/bin/env python3
""" Module for print a safe print division"""


def safe_print_division(a, b):
    """ Print a / b and return the result """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
