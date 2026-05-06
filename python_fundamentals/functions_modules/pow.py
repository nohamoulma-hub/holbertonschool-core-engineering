#!/usr/bin/env python3

def pow(a, b):

    if b == 0:
        return 1
    elif b > 0:
        exposant = b
    else:
        exposant = -b

    result = 1
    for i in range(exposant):
        result = result * a

    if b < 0:
        return 1 / result

    return result
