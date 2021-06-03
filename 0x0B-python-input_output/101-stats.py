#!/usr/bin/python3
"""This script reads stdin line by line and
Each 10 lines and after a keyboard interruption (CTRL + C)
prints those statistics since the beginning"""
import sys


def prints_statistics(statuses, size):
    print("File size: {}".format(size))

    for status, quantity in sorted(statuses.items()):
        if quantity > 0:
            print("{}: {}".format(status, quantity))

valid_status = {
    200: 0, 301: 0, 400: 0, 401: 0,
    403: 0, 404: 0, 405: 0, 500: 0
}

status = 0
size = 0
count = 0

try:
    for line in sys.stdin:
        count += 1
        statistics = [int(s) for s in line.split() if s.isdigit()]
        size += statistics[1]
        valid_status[statistics[0]] += 1

        if count % 10 == 0:
            prints_statistics(valid_status, size)
except KeyboardInterrupt:
    prints_statistics(valid_status, size)
