import math as m
import error_helper_by_delica as error_lib


def find_num_integer_digits(val):
    """Finds the number of integer digits in a float or integer value.

    Note: This function defines the number of integer digits in 0 as zero. Values 1-9.999... have one integer digit,
    10-99.999... have two, etc. The same rules apply for negative values.

    Parameters
    ----------
    val : float | int
        The value in which we should find the number of integer digits.

    Returns
    -------
    num_integer_digits : int
        The number of integer digits in the provided float or integer value.

    Raises
    ------
    TypeError
        Raised if the value to round is not a float or integer.
    """
    error_lib.check_type(val, float, "find integer digits value", alt_type=int)
    int_val = abs(int(val))
    num_integer_digits = 0
    if int_val > 0:
        num_integer_digits = int(m.log10(int_val)) + 1
    return num_integer_digits
#
# def find_num_decimal_digits(val):
#     error_lib.check_type(val, float, "find decimal digits value", alt_type=int)
#     int_val = int(val)
#     val_no_int = val-int_val
#     abs_val_no_int = abs(val_no_int)
#     num_decimal_digits = 0
#     if abs_val_no_int > 0:
#
#
#     return num_decimal_digits



def round_to_precision(val, prec):
    """Rounds a float or integer value to a specified precision.

    Parameters
    ----------
    val : float | int
        The value to round.
    prec : float | int
        The smallest base-10 order of magnitude at which we can measure the value (e.g, 10 if we should round to the
        tens place, 1 if we should round to the ones place, 0.1 if we should round to the tenths place, 0.01 if we
        should round to the hundredths place, etc.). Please note that this value cannot be zero or negative.

    Returns
    -------
    rounded_val : float | int
        The rounded value.

    Raises
    ------
    TypeError
        Raised if the value to round is not a float or integer, the precision is not a float or integer, or the
        precision is negative or zero.
    """
    error_lib.check_type(val, float, "value to round", alt_type=int)
    result = val
    if prec != -1:
        error_lib.check_type(prec, float, "rounding precision", alt_type=int)
        error_lib.check_value_is_positive(prec, "rounding precision")
        int_val = int(val)
        if prec == 1:
            result = int_val
        else:
            prec_log = int(m.log10(prec))
            if prec_log >= 0:
                result = round(int_val, -prec_log)
            else:
                result = round(val, -prec_log)
    return result


def get_num_leading_decimal_zeros(float_val, prec):
    num_leading_zeros = 0
    abs_float_val = abs(float_val)
    if abs_float_val < 1.0:
        num_multiplies = 0
        max_num_multiplies = int(-m.log10(prec))
        temp_val = abs_float_val
        while temp_val < 1 and num_multiplies < max_num_multiplies:
            temp_val *= 10.0
            num_multiplies += 1
        num_leading_zeros = num_multiplies - 1
        test = 0
    return num_leading_zeros

# result = get_num_leading_decimal_zeros(1.01, 0.1)
# test = 0

def get_num_sig_figs(val, prec):
    result = 0
    num_integer_digits = find_num_integer_digits(val)
    num_int_sig_figs = 0
    if prec <= 1:
        num_int_sig_figs = num_integer_digits
    else:
        num_int_sig_figs = num_integer_digits - int(m.log10(prec))
    num_float_sig_figs = 0
    if prec < 1:
        num_float_sig_figs = int(-1*m.log10(prec))
    if num_int_sig_figs == 0:
        num_leading_zeros = get_num_leading_decimal_zeros(val, prec)
        result = num_float_sig_figs - num_leading_zeros
    else:
        result = num_int_sig_figs + num_float_sig_figs
    return result

# result = get_num_sig_figs(0.05, 0.01)
# test = 0

def add_vals_with_sig_figs(val_1, val_2, val_1_prec=-1, val_2_prec=-1):
    error_lib.check_type(val_1, float, "Value 1 (in add with sig figs)", alt_type=int)
    error_lib.check_type(val_2, float, "Value 2 (in add with sig figs)", alt_type=int)
    error_lib.check_type(val_1_prec, float, "Value 1 Precision (in add with sig figs)", alt_type=int)
    if val_1_prec != -1:
        error_lib.check_value_is_positive(val_1_prec, "Value 1 Precision")
    error_lib.check_type(val_2_prec, float, "Value 2 Precision (in add with sig figs)", alt_type=int)
    if val_2_prec != -1:
        error_lib.check_value_is_positive(val_2_prec, "Value 2 Precision")
    unrounded_result = val_1 + val_2
    result_val = unrounded_result
    result_num_sig_figs = -1
    if val_1_prec != -1 or val_2_prec != -1:
        bigger_prec = val_1_prec
        if val_1_prec == -1:
            bigger_prec = val_2_prec
        if val_1_prec != -1 and val_2_prec != -1:
            if val_1_prec > val_2_prec:
                bigger_prec = val_1_prec
            else:
                bigger_prec = val_2_prec
        result_val = round_to_precision(unrounded_result, bigger_prec)
        result_num_sig_figs = get_num_sig_figs(unrounded_result, bigger_prec)
    return result_val, result_num_sig_figs




def rect_area(length, width, length_prec, width_prec):
    product = length * width
