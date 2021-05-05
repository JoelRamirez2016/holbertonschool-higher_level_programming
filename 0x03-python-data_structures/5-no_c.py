#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for c in my_string:
        if c not in "cC":
            str += c
    return str
