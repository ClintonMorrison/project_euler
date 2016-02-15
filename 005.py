"""
This file contains a solution for the fifth Project Euler problem.
https://projecteuler.net/problem=5

Author: Clinton Morrison
File:   005.py
"""
import util

lcm_factors = {}

for a in xrange(1, 21):
    for (factor, count) in util.factor(a).iteritems():
        lcm_factors[factor] = max(count, lcm_factors.get(factor, 0))

result = 1
for (factor, count) in lcm_factors.iteritems():
    result *= factor**count

print result

