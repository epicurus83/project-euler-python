import math

"""
Solution 2

According to the benchmark this has O(n) complexity but it is faster than solution 1.
"""


def solution_2(upper_bound):
    if upper_bound < 3:
        raise Exception("Input number must be greater than 3.")

    _sum_of_multiples = 0

    _sum_of_multiples += _get_sum_of_multiple(upper_bound, 3)
    _sum_of_multiples += _get_sum_of_multiple(upper_bound, 5)
    _sum_of_multiples -= _get_sum_of_multiple(upper_bound, 15)

    return _sum_of_multiples


def _get_sum_of_multiple(upper_bound, multiple):
    _iterations = math.ceil(upper_bound / multiple)
    _multiplication_number = 0

    for i in range(1, _iterations):
        _multiplication_number += i

    return _multiplication_number * multiple
