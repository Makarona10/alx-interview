#!/usr/bin/python3

def square_root(val):
    ans = 1
    sqr = 1
    i = 1
    while (sqr <= val):
        i += i
        sqr = i * i
    ans = i - 1
    return ans


def get_primes(n):
    if n <= 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, square_root(n)):
        if is_prime[i]:
            for x in range(i * i, n, i):
                is_prime[x] = False

    return len([i for i in range(n) if is_prime[i]])


def isWinner(x, nums):
    maria = 0
    ben = 0
    winner = None
    for i in range(x):
        primes = get_primes(nums[i])
        if primes % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        winner = 'Maria'
    elif maria > ben:
        winner = 'Ben'
    return winner
