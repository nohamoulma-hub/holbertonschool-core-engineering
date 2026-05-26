#!/usr/bin/env python3
""" Module add a string in a file"""


def write_file(filename="", text=""):
    """ Write text in a exist file or create if not exist"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
