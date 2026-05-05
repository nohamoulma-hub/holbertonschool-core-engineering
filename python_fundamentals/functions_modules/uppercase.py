#!/usr/bin/env python3
def uppercase(str):
    for i in str:
        if i >= 97 and i <= 122:
            print("{}".format(chr(ord(i) - 32)), end="")
        else:
            print("{}".format(i), end="")
