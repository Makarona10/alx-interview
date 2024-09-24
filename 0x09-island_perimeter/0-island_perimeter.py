#!/usr/bin/python3
'''0x09. Island Perimeter'''


def island_perimeter(grid):
    ribs = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                if grid[row-1][col] == 0:
                    ribs += 1
                if grid[row+1][col] == 0:
                    ribs += 1
                if grid[row][col+1] == 0:
                    ribs += 1
                if grid[row][col-1] == 0:
                    ribs += 1
    return ribs
