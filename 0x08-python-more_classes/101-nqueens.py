#!/usr/bin/python3
import sys


def is_in(pos, lines):
    return False


"""
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit()

try:

    N = int(sys.argv[1])

except (ValueError):
    print("N must be a number")
    exit()

if N < 4:
    print("N must be at least 4")
    exit()
"""
N = 6

print("working {:d}".format(N))

closed_points = []
points = []



for i in range(N):
    for k in range(0, N):
        if i == 0 and k == 0:
            continue

        point = [i, k]

        if point in closed_points:
            continue

        row_v = [[i, j] for j in range(0, N)]
        row_h = [[j, k] for j in range(0, N)]
        row_dd = [[i + j, k + j] for j in range(0, N) if i + j < N and k + j < N]
        row_di = [[i + j, k - j] for j in range(0, N) if k - j >= 0 and i + j < N]
        closed_points = closed_points + row_v + row_h + row_dd + row_di
        points.append(point)

    for point in points:
        

print(points)
