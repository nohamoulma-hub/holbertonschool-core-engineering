#!/usr/bin/env python3
def safe_print_list(my_list=[], x=0):
    try:
        print(my_list[x])
    except IndexError:
        return my_list
