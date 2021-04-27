#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1):
    if chr(c) not in "qe":
        print("{:c}".format(c), end="")
