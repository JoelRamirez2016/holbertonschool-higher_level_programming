#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if row:
            print("{:d}".format(row[0]), end="")
            for i in range(1, len(row)):
                print(" {:d}".format(row[i]), end="")
        print("")
