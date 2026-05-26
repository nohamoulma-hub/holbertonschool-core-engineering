#!/usr/bin/env python3
""" """

def read_file(filename=""):
    """ """
    with open(filename, encoding="uft-8") as f:
        print(f.read(), end="")
