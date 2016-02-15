"""
This file contains some functions that are useful for
many Project Euler problems.

Author: Clinton Morrison
File: util.py
"""
import math


def gcd(a, b):
    t = 0
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def lcm(a, b):
    return a*b / gcd(a, b)


def factor(n, factSoFar = None):
    if not factSoFar:
        factSoFar = {}

    if n <= 1:
        return factSoFar

    sqrt_n = int(math.ceil(math.sqrt(n)))
    for i in xrange(2, sqrt_n+1):

        if n % i == 0:
            factSoFar[i] = factSoFar.get(i, 0) + 1
            n = int(math.floor(n/i))
            return factor(n, factSoFar)

    factSoFar[n] = factSoFar.get(n, 0) + 1
    return factSoFar


def is_prime(n):
    factors = factor(n)
    return len(factors.keys()) == 1 and factors.get(factors.keys()[0], 0) == 1


# An inefficient method to generate primes <= n
def primes_up_to(n):
    primes = []
    for i in xrange(1, n+1):
        if is_prime(i):
            primes.append(i)
    return primes

def sieve(n):
    nums = [True] * (n-1)  # True -> prime

    for i, prime in enumerate(nums):
        if not prime:
            continue

        j = i + i + 2
        while j < len(nums):
            nums[j] = False
            j += (i+2)
    return [i+2 for (i, prime) in enumerate(nums) if prime]