#!/usr/bin/env python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    key_max_value = max(a_dictionary.values())
    for i in a_dictionary:
        if a_dictionary[i] == key_max_value:
            return i
