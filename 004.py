"""
This file contains a solution for the fourth Project Euler problem.
https://projecteuler.net/problem=4

Author: Clinton Morrison
File:   004.py
"""


# Returns True is string is palindrome
def is_palindrome(s):
    for i in xrange(len(s)/2):
        if s[i] != s[-(i + 1)]:
            return False
    return True


# Finds the largest palindrome that is a product of
# two integers of n digits
def find_largest(n):
    largest = 0

    start = 10**(n-1)
    end = 10**(n)

    for a in reversed(xrange(start, end)):
        for b in reversed(xrange(start, end)):
            if is_palindrome(str(a*b)):
                largest = a*b if a*b > largest else largest
    return largest


print find_largest(3)