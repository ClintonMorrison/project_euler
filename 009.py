"""
This file contains a solution for the ninth Project Euler problem.
https://projecteuler.net/problem=9

Author: Clinton Morrison
File:   009.py
"""
import sys
import math


for a in xrange(1, 1000):
    for b in xrange(1, 1000):
        c2 = a**2 + b**2
        c = math.sqrt(c2)
        if math.floor(c) == c:
            if a+b+c == 1000:
                print 'a*b*c =', a*b*c
                sys.exit()