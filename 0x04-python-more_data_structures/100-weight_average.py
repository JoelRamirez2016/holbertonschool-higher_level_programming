#!/usr/bin/python3
def weight_average(my_list=[]):
    mul = 0
    div = 0
    for tup in my_list:
        mul += tup[0] * tup[1]
        div += tup[1]
    return mul / (div if div else 1)
