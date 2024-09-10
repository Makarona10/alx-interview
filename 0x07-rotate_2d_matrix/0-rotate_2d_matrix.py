#!/usr/bin/python3
"""Test 0x07 - Rotate 2D Matrix"""


def rotateMatrix(mat):
    n = len(mat)
    for x in range(0, int(n / 2)):

        for y in range(x, n-x-1):

            temp = mat[x][y]
            mat[x][y] = mat[y][n-1-x]
            mat[y][n-1-x] = mat[n-1-x][n-1-y]
            mat[n-1-x][n-1-y] = mat[n-1-y][x]
            mat[n-1-y][x] = temp
