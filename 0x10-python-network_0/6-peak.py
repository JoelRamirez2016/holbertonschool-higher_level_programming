#!/usr/bin/python3
"""This module define the function find_peak"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if list_of_integers == []:
        return None

    if len(list_of_integers) <= 2:
        return max(list_of_integers)

    mid_i = int(len(list_of_integers) / 2)

    if list_of_integers[mid_i] < list_of_integers[mid_i - 1]:
        return find_peak(list_of_integers[:mid_i])

    if list_of_integers[mid_i] < list_of_integers[mid_i + 1]:
        return find_peak(list_of_integers[mid_i + 1:])

    return list_of_integers[mid_i]
