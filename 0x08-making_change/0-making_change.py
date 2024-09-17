#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    min = -1
    for n in coins:
        sum = n
        count = 1
        i = 0
        while i < len(coins):
            if sum + coins[i] <= total:
                sum += coins[i]
                count += 1
            else:
                i += 1
            if sum == total:
                if count < min or min == -1:
                    min = count
                sum = n
                i += 1
                count = 1
    return min
