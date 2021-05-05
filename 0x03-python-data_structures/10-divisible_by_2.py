#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    modules = []
    for i in my_list:
        modules.append(i % 2 == 0)
    return modules
