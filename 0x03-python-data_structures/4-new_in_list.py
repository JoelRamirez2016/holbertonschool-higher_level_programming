#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp_l = my_list.copy()
    if idx >= 0 and idx < len(my_list):
        cp_l[idx] = element
    return cp_l
