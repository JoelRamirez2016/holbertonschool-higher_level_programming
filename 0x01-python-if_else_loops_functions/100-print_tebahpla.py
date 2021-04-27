#!/usr/bin/python3
up = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(c - up), end="")
    if up == 0:
        up = 32
    else:
        up = 0
