#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_l = my_list.copy()
    for i in range(0, len(new_l)):
        if search == new_l[i]:
            new_l[i] = replace
    return new_l
