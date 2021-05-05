#!/usr/bin/python3
def max_integer(my_list=[]):
    mx = 0

    if not my_list:
        return None
    for i in my_list:
        mx = i if i > mx else mx
    return mx
