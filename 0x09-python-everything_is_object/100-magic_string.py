#!/usr/bin/python3
def magic_string():
    magic_string.iterator = getattr(magic_string, 'iterator', 0) + 1
    return (magic_string.iterator - 1) * "Holberton, " + "Holberton"
