#!/usr/bin/python3
import sys


def queens(N, solutions, pieces=0, positions=[])
    if N == pieces:
        solutions.append(positions.copy())

    for i in range(N):
        positions.append(i)

        if (check_queens(i, positions)):
            queens(N, solutions, pieces + 1, positions)

        positions.pop(-1)

def check_queens(p, positions):

    for i in range(p):
        if positions[i] == positions[p] or positions[i] == positions[p] + 1:
            return False

    return True

"""
            row_v = [[i, j] for j in range(0, N)]
            row_h = [[j, k] for j in range(0, N)]
            row_dd = [[i + j, k + j] for j in range(0, N) if i + j < N and k + j < N]
            row_di = [[i + j, k - j] for j in range(0, N) if k - j >= 0 and i + j < N]
            closed_points.append( (point, row_v + row_h + row_dd + row_di))


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

queens(N)

print(points)
