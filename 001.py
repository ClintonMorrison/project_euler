"""
This file contains a solution for the first Project Euler problem.
https://projecteuler.net/problem=1

Author: Clinton Morrison
File:   001.py
"""
import util

print sum([x for x in xrange(1, 1001) if util.gcd(x, 15) > 1])
