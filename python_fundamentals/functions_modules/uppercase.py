#!/usr/bin/env python3
def uppercase(str):
    for i in str:
        if str >= 97 and str <= 122:
            chr(ord(i) - 32)
        else:
            print("{}".format(i))
