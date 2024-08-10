#!/usr/bin/python3

""" 0x02-minimum_operations Project """


def isPrime(n: int) -> bool:
    for i in range(2, int(n/2)):
        if n % i == 0:
            return False
    return True


def minOperations(n: int) -> int:
    if (type(n) is not int) or (n <= 1):
        return 0
    if isPrime(n):
        return n
    if n % 2 == 0:
        if isPrime(n // 2):
            return int(n // 2) + 2
        return 2 + minOperations(n // 2)
    else:
        steps = 2
        step = 1
        i = 2
        while (i < n):
            if n % i == 0:
                step = i
                steps += 2
                i *= 2
            i += step
            steps += 1
    return steps
