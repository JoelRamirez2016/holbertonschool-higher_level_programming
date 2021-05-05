#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp_l = my_list.copy()
    if idx > 0 or idx < len(my_list) - 1:
        cp_l[idx] = element
    return cp_l
