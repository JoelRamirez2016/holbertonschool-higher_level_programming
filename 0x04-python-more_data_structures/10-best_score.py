#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        mx_k = list(a_dictionary.keys())[0]
        for key in a_dictionary:
            mx_k = key if a_dictionary[mx_k] <= a_dictionary[key] else mx_k
        return mx_k
    return None
