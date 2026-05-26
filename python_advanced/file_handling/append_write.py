#!/usr/bin/env python3
""" Module add a string in a file"""


def append_write(filename="", text=""):
    """ add a string at the end"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
