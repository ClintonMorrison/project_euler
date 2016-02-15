"""
This file contains a solution for the seventh Project Euler problem.
https://projecteuler.net/problem=7

Author: Clinton Morrison
File:   007.py
"""
import util

primes = util.sieve(200000)
print primes[10000]