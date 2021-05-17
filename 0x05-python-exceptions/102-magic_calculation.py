#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(0, 103):
        try:
            result = a + b
            break
        except:
            if i > a:
                raise Exception('Too far')
            else:
                result = (a ** b / i) + result
            continue
    return result
