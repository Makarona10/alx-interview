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
    if isPrime(n/2):
        return int(n/2) + 2
    if n % 2 == 0:
        return 1 + minOperations(n / 2)
    # else:
    #     steps = n
    #     for i in range(1, )

print(minOperations(28))