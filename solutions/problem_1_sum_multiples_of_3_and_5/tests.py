import unittest

from solutions.problem_1_sum_multiples_of_3_and_5.solution_1 import solution_1
from solutions.problem_1_sum_multiples_of_3_and_5.solution_2 import solution_2
from solutions.problem_1_sum_multiples_of_3_and_5.solution_3 import solution_3

_solutions = [solution_1, solution_2, solution_3]


class MyTestCase(unittest.TestCase):
    def test_1_input_below_2_raises_exception(self):
        for _solution in _solutions:
            with self.assertRaises(Exception):
                _solution(2)

    def test_2_input_number_x_returns_y(self):
        for _solution in _solutions:
            print("testing: ", _solution.__name__)
            self.assertEqual(23, _solution(10))
            self.assertEqual(78, _solution(20))
            self.assertEqual(2318, _solution(100))


if __name__ == '__main__':
    unittest.main()
