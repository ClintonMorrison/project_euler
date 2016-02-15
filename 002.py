"""
This file contains a solution for the second Project Euler problem.
https://projecteuler.net/problem=2

Author: Clinton Morrison
File:   002.py
"""


def generate_fib(max):
    result = [1, 2]
    while result[-1] + result[-2] <= max:
        result.append(result[-1] + result[-2])
    return result

print sum([x for x in generate_fib(4000000) if x % 2 == 0])