#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    r = []
    val = 0
    for i in range(0, list_length):
        try:
            val = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError):
            print("division by 0")
            val = 0
        except (TypeError):
            print("wrong type")
            val = 0
        except (IndexError):
            print("out of range")
            val = 0
        finally:
            r.append(val)
    return r
