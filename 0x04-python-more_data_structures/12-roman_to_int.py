#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }
    n = 0
    if roman_string:
        for roman_n in roman_string:
            if n >= roman_d[roman_n] or n == 0:
                n += roman_d[roman_n]
            else:
                n = roman_d[roman_n] - n
        return (n)
    return (0)
