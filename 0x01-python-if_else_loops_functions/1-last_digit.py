#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastD = abs(number) % 10 if number > 0 else -(abs(number) % 10)

print("Last digit of {} is", end="")

if lastD > 5:
    print("{} and is greater than 5".format(number, lastD))
elif lastD == 0:
    print("{} and is 0".format(number, lastD))
else:
    print("{} and is less than 6 and not 0".format(number, lastD))
