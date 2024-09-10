#!/usr/bin/python3
"""Test 0x07 - Rotate 2D Matrix"""


def rotate(matrix, t):
    if t == 0:
        return

    n = len(matrix)
    for x in range(0, int(n / 2)):

        for y in range(x, n-x-1):

            temp = matrix[x][y]
            matrix[x][y] = matrix[y][n-1-x]
            matrix[y][n-1-x] = matrix[n-1-x][n-1-y]
            matrix[n-1-x][n-1-y] = matrix[n-1-y][x]
            matrix[n-1-y][x] = temp
    rotate(matrix, t - 1)


def rotate_2d_matrix(matrix):
    rotate(matrix, 3)
