"""Script to test the functions in the math helper package (math_helper_funcs.py)."""

import math_helper_by_delica as math_lib
import test_helper_by_delica as test_lib
from test_helper_by_delica.IOPair import IOPair

run_all_tests = False
"bool : Boolean flag for whether all tests should be run, regardless of their boolean flags below."

test_find_num_integer_digits = False
"bool : Boolean flag for whether or not to run the tests for the find_num_integer_digits function."
test_round_to_precision = True
"bool : Boolean flag for whether or not to run the tests for the round_to_precision function."


if test_find_num_integer_digits or run_all_tests:
    test_lib.run_func_tests(math_lib.find_num_integer_digits, [
        IOPair((0,), (0,)),
        IOPair((1,),(1,)),
        IOPair((5,), (1,)),
        IOPair((10,), (2,)),
        IOPair((100,), (3,)),
        IOPair((109,), (3,)),
        IOPair((-1,), (1,)),
        IOPair((-5,), (1,)),
        IOPair((-10,), (2,)),
        IOPair((-100,), (3,)),
        IOPair((-109,), (3,)),
    ])

