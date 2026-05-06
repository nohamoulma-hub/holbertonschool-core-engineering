#!/usr/bin/env python3

def pow(a, b):
    result = 1
    for i in range(b):
        if b <= 0:
            print(1)
        result = result * a
    return result
