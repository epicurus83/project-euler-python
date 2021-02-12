import math

"""
Solution 3

We use the formula for the sum of an arithmetic series: n/2*(a_1 + a_n).
Where n is the upper bound, a_1 is first element in the sequence and a_n is the last element in the sequence.
To avoid rounding errors, instead of dividing by two we will perform bitwise right shift of 1 digit.
This is very fast and O(1) constant time complexity.
"""


def solution_3(upper_bound):
    if upper_bound < 3:
        raise Exception("Input number must be greater than 3.")

    upper_bound -= 1

    _sum_of_multiples_of_3 = _get_multiple_contribution(upper_bound, 3)
    _sum_of_multiples_of_5 = _get_multiple_contribution(upper_bound, 5)
    _sum_of_multiples_of_15 = _get_multiple_contribution(upper_bound, 15)

    return int(int(_sum_of_multiples_of_3 + _sum_of_multiples_of_5 - _sum_of_multiples_of_15) >> 1)


def _get_multiple_contribution(upper_bound, multiple):
    return multiple * _double_sum_arithmetic_series(_get_number_of_terms(upper_bound, multiple))


def _get_number_of_terms(upper_bound, multiple):
    return int(upper_bound / multiple)


def _double_sum_arithmetic_series(number_of_terms):
    return number_of_terms * (1 + number_of_terms)
