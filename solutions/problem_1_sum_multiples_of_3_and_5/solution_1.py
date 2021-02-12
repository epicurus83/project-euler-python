import math

""" 
Solution 1

Brute Force Algorithm.
This is a bad solution it is O(n) complexity but it is still very slow
"""


def solution_1(upper_bound):
    if upper_bound < 3:
        raise Exception("Input number must be greater than 3.")

    _sum_of_multiples = 0

    for i in range(3, upper_bound):
        if i % 3 == 0 or i % 5 == 0:
            _sum_of_multiples += i

    return _sum_of_multiples
