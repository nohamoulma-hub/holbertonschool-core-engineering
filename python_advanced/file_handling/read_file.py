#!/usr/bin/env python3
""" Module who read a file"""


def read_file(filename=""):
    """ read a file """
    with open(filename, encoding="uft-8") as f:
        print(f.read(), end="")
