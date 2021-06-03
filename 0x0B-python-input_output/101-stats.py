#!/usr/bin/python3
"""This script reads stdin line by line and
Each 10 lines and after a keyboard interruption (CTRL + C)
prints those statistics since the beginning"""
import sys


def prints_statistics(statuses, size):
    """shows stored counts and total size
    Args:
        statuses (dict): dict of status to print
        size (int): cumulative size by requests
    """
    print("File size: {}".format(size))

    for status, quantity in sorted(statuses.items()):
        if quantity > 0:
            print("{}: {}".format(status, quantity))

if __name__ == '__main__':

    valid_status = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }

    size = 0
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            statistics = [int(s) for s in line.split() if s.isdigit()]

            try:
                size += statistics[1]

                if statistics[0] in valid_status:
                    valid_status[statistics[0]] += 1
            except:
                pass

            if count % 10 == 0:
                prints_statistics(valid_status, size)

        prints_statistics(valid_status, size)
    except KeyboardInterrupt:
        prints_statistics(valid_status, size)
        raise
