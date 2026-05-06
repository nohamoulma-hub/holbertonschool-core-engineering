#!/usr/bin/env python3

def pow(a, b):
    exposant = b
    if b < 0:
        b = -b

    result = 1

    for i in range(exposant):
        if b <= 0:
            return 1
        result = result * a

    return result
