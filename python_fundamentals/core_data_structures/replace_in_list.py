#!/usr/bin/env python3
def replace_in_list(my_list, idx, element):
    taille = len(my_list)
    if idx < 0 or idx >= taille:
        return my_list[idx]
    else:
        my_list.replace(idx, element)
        return my_list[element]
