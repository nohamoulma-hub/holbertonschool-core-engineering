#!/usr/bin/env pyhton3
def safe_print_list(my_list=[], x=0):
    try:
        print(my_list[x])
    except ZeroDivisionError:
        return my_list
