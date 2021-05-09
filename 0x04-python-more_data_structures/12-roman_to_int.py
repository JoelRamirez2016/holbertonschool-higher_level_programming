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
    sums = 0
    if type(roman_string) == str:
        for roman_n in roman_string:
            if roman_n not in roman_d:
                return 0

        for i in range(0, len(roman_string)):
            if len(roman_string) != i + 1 and \
               roman_d[roman_string[i]] < roman_d[roman_string[i + 1]]:
                sums += -roman_d[roman_string[i]]
            else:
                sums += roman_d[roman_string[i]]
        return sums
    return 0
