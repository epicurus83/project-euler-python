import math

"""
Solution 3

We use the formula for the sum of an arithmetic series: n/2*(a_1 + a_n).
Where n is the upper bound, a_1 is first element in the sequence and a_n is the last element in the sequence.
This is very fast and O(1) constant time complexity.
"""


def solution_3(upper_bound):
    if upper_bound < 3:
        raise Exception("Input number must be greater than 3.")

    _sum_of_multiples_of_3 = 3 * _sum_arithmetic_series(_get_number_of_terms(upper_bound, 3))
    _sum_of_multiples_of_5 = 5 * _sum_arithmetic_series(_get_number_of_terms(upper_bound, 5))
    _sum_of_multiples_of_15 = 15 * _sum_arithmetic_series(_get_number_of_terms(upper_bound, 15))

    return _sum_of_multiples_of_3 + _sum_of_multiples_of_5 - _sum_of_multiples_of_15


def _get_number_of_terms(upper_bound, multiple):
    return math.floor((upper_bound - 1) / multiple)


def _sum_arithmetic_series(number_of_terms):
    return (number_of_terms * (1 + number_of_terms)) / 2
