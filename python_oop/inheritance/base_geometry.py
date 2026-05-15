#!/usr/bin/env python3
""" creation of new class basegeometry"""


class BaseGeometry:
    """Class who define geometry shapes"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))
