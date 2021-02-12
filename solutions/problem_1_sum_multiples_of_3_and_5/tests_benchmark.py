import unittest

from solutions.problem_1_sum_multiples_of_3_and_5.solution_1 import solution_1
from solutions.problem_1_sum_multiples_of_3_and_5.solution_2 import solution_2
from solutions.problem_1_sum_multiples_of_3_and_5.solution_3 import solution_3
import timeit, functools

_solutions = [solution_1, solution_2, solution_3]


class MyTestCase(unittest.TestCase):
    def test_benchmark(self):
        _inputs = [100, 200, 400, 800, 1600]
        _times = []
        print("Running benchmark...")
        for _solution in _solutions:
            for input in _inputs:
                _time_execution_function(_solution, input, _times)
            print("%s benchmark" % _solution.__name__)
            _print_benchmark_numbers(_inputs, _times)


def _time_execution_function(solution_func, input, times):
    _time_for_execution_in_seconds = timeit.Timer(functools.partial(solution_func, input)).timeit()
    times.append(_time_for_execution_in_seconds)


def _print_benchmark_numbers(inputs, times):
    for i in range(0, len(inputs)):
        print("input: %d, time(s): %d" % (inputs[i], times[i]))


if __name__ == '__main__':
    unittest.main()
