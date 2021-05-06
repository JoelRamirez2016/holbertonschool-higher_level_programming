#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = a_dictionary.copy()
    for key in new_d:
        new_d[key] = new_d[key] * 2
    return new_d
