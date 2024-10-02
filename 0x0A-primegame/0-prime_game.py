#!/usr/bin/python3

"""0x0A. Prime Game problem"""


def square_root(val):
    """Gets the square root of a number (similar to math.isqrt)"""
    ans = 1
    sqr = 1
    i = 1
    while (sqr <= val):
        i += i
        sqr = i * i
    ans = i - 1
    return ans


def get_primes(n):
    """Get a list of prime numbers less than or equal to a specific number n"""
    if n < 2:
        return []

    is_prime = [True] * (n + 1)  # Include n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for x in range(i * i, n + 1, i):  # Ensure multiples of i are marked
                is_prime[x] = False

    # return [i for i in range(n + 1) if is_prime[i]]
    return len([i for i in range(n) if is_prime[i]])


def isWinner(x, nums):
    """Determines who is the winner of prime game"""
    maria = 0
    ben = 0
    winner = None
    for i in range(x):
        primes = get_primes(nums[i] + 1)
        if primes % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        winner = 'Ben'
    elif maria > ben:
        winner = 'Maria'
    return winner
