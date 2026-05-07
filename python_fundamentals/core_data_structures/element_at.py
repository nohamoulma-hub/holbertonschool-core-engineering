#!/usr/bin/env python3
def element_at(my_list, idx):
    for idx in my_list:
        if idx < 0 or idx > 5:
            return None
        else:
            print("{}".format(idx))


if __name__ == "__main__":
    element_at(my_list=[], idx=[])
