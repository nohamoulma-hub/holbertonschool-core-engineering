#!/usr/bin/env python3

def pow(a, b):

    exposant = b

    if b < 0:
        b = -b
    if b == 0:
        return 1
    
    result = 1
    for i in range(exposant):
        result = result * a
        if b < 0:
            return 1 / result

    return result
