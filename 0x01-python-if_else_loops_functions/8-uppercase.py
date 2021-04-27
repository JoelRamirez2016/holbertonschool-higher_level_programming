#!/usr/bin/python3
def uppercase(str):
    word = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            word += chr(ord(c) - 32)
        else:
            word += c
    print("{}".format(word))
