"""
This file contains a solution for the sixth Project Euler problem.
https://projecteuler.net/problem=6

Author: Clinton Morrison
File:   006.py
"""

total = 0
squares = 0
for x in xrange(1, 101):
    squares += x**2
    total += x

print total**2 - squares