#!/usr/bin/env python3
def replace_in_list(my_list, idx, element):
    taille = len(my_list)
    if idx < 0 or idx >= my_list:
        return my_list[idx]
    else:
        idx = element
        return my_list[element]
