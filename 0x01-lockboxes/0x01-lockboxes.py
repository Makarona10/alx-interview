#!/usr/bin/python3

'''Boxes unlock problem'''


def canUnlockAll(boxes):
    keys = [0]
    boxesNumber = len(boxes)
    for i in range(boxesNumber):
        for key in boxes[i]:
            if key != i and key not in keys:
                keys.append(key)
            if len(keys) == boxesNumber:
                return True
    return False

boxes = [[1], [2], [3], [4], []]

print(canUnlockAll(boxes))