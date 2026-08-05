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
test_get_num_leading_decimal_zeros = True
"bool : Boolean flag for whether or not to run the tests for the get_num_leading_decimal_zeros function."
test_get_num_sig_figs = True
"bool : Boolean flag for whether or not to run the tests for the get_num_sig_figs function."


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

if test_round_to_precision or run_all_tests:
    test_lib.run_func_tests(math_lib.round_to_precision, [
        IOPair((0, 1), (0,)),
        IOPair((0, 2), (0,)),
        IOPair((0, 0.1), (0,)),
        IOPair((0, 0.01), (0,)),
        IOPair((0.2, 1), (0,)),
        IOPair((0.7, 1), (1,)),
        IOPair((1.1, 1), (1,)),
        IOPair((1.9, 1), (2,)),
        IOPair((115, 1), (115,)),
        IOPair((115, 0.1), (115.0,)),
        IOPair((116, 10), (120,)),
        IOPair((116, 100), (100,)),
        IOPair((1162728.00023, 0.0001), (1162728.0002,)),
        IOPair((-0.2, 1), (0,)),
        IOPair((-0.7, 1), (-1,)),
        IOPair((-1.1, 1), (-1,)),
        IOPair((-1.9, 1), (-2,)),
        IOPair((-115, 1), (-115,)),
        IOPair((-115, 0.1), (-115.0,)),
        IOPair((-116, 10), (-120,)),
        IOPair((-116, 100), (-100,)),
        IOPair((-1162728.00023, 0.0001), (-1162728.0002,)),
    ])

if test_get_num_leading_decimal_zeros or run_all_tests:
    test_lib.run_func_tests(math_lib.get_num_leading_decimal_zeros, [
        IOPair((1,), (0,)),
        IOPair((10,), (0,)),
        IOPair((0.1,), (0,)),
        IOPair((0.01,), (1,)),
        IOPair((0.001,), (2,)),
        IOPair((-1,), (0,)),
        IOPair((-10,), (0,)),
        IOPair((-0.1,), (0,)),
        IOPair((-0.01,), (1,)),
        IOPair((-0.001,), (2,)),
        IOPair((9,), (0,)),
        IOPair((90,), (0,)),
        IOPair((0.9,), (0,)),
        IOPair((0.09,), (1,)),
        IOPair((0.009,), (2,)),
        IOPair((-9,), (0,)),
        IOPair((-90,), (0,)),
        IOPair((-0.9,), (0,)),
        IOPair((-0.09,), (1,)),
        IOPair((-0.009,), (2,)),
    ])

if test_get_num_sig_figs or run_all_tests:
    test_lib.run_func_tests(math_lib.get_num_sig_figs, [
        IOPair((0, 1), (0,)),
        IOPair((0.0,1), (0,)),
        IOPair((1, 1), (1,)),
        IOPair((2, 1), (1,)),
        IOPair((10, 10), (1,)),
        IOPair((10, 1), (2,)),
        IOPair((101290, 10), (5,)),
        IOPair((9909.0, 0.1), (5,)),
        IOPair((0.0023, 0.001), (1,)),
        IOPair((0.0023, 0.0001), (2,)),
        IOPair((-1, 1), (1,)),
        IOPair((-2, 1), (1,)),
        IOPair((-10, 10), (1,)),
        IOPair((-10, 1), (2,)),
        IOPair((-101290, 10), (5,)),
        IOPair((-9909.0, 0.1), (5,)),
        IOPair((-0.0023, 0.001), (1,)),
        IOPair((-0.0023, 0.0001), (2,)),
        IOPair((0, 0), (ValueError,)),
        IOPair((0, -1), (ValueError,)),
    ])