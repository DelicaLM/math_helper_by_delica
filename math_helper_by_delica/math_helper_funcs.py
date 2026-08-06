import math
import math as m
import error_helper_by_delica as error_lib

PI = m.pi


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
        Raised if the value to round is not a float or integer or the precision is not a float or integer.
    ValueError
        Raised if the precision is negative or zero.
    """
    error_lib.check_type(val, float, "value to round", alt_type=int)
    result = val
    if prec != -1:
        error_lib.check_type(prec, float, "rounding precision", alt_type=int)
        error_lib.check_value_is_positive(prec, "rounding precision")
        int_val = int(val)
        if prec == 1:
            result = round(val)
        else:
            prec_log = int(m.log10(prec))
            if prec_log >= 0:
                result = round(int_val, -prec_log)
            else:
                result = round(val, -prec_log)
    return result

def round_to_num_sig_figs(val, num_sig_figs):
    """Rounds a float or integer value to a specified number of significant figures.

    Parameters
    ----------
    val : float | int
        The value to round.
    num_sig_figs : int
        The number of significant figures that should be in the rounded value (must be a positive integer).

    Returns
    -------
    rounded_val : float | int
        The rounded value.

    Raises
    ------
    TypeError
        Raised if the value to round is not a float or integer, the number of significant figures is not an integer.
    ValueError
        Raised if the number of significant figures negative or zero.
    """
    error_lib.check_type(val, float, "value to round", alt_type=int)
    error_lib.check_type(num_sig_figs, int, "number of significant figures")
    error_lib.check_value_is_positive(num_sig_figs, "number of significant figures")
    result = val
    num_integer_digits = find_num_integer_digits(val)
    if num_integer_digits == num_sig_figs:
        result = round_to_precision(val, 1)
    elif num_integer_digits > num_sig_figs:
        left_out_digits = num_integer_digits - num_sig_figs
        result = round_to_precision(val, 10**left_out_digits)
    else:
        num_float_digits = num_sig_figs - num_integer_digits
        result = round_to_precision(val, 0.1**num_float_digits)
    return result


def get_num_leading_decimal_zeros(float_val, prec=-1):
    """Calculates the number of leading decimal zeros in a float value.

    For example, 0.1 has zero leading decimal zeros, 0.01 has one, 0.001 has two, and so on.

    Parameters
    ----------
    float_val : float | int
        The float value in which we should find the number of leading decimal zeros. If an integer is provided, the
        returned number of leading decimal zeros will always be zero (because an integer does not have a fractional
        component).
    prec : float | int, default -1
        The precision of the float value (i.e. the smallest base-10 order of magnitude at which we can measure
        the float value, such as 1 if we only know the number to the ones place, 10 if we know it to the tens, 0.1 if
        we know it the tenths, 0.01 if we know it to the hundredths, etc.). If the value is known to an infinite
        precision (e.g., for universal constants), one can use the default precision value (-1). However, the actual
        precision used in this default case will be 10^-15, because values below 10^-15 in Python are highly
        susceptible to numerical errors. If you are not using the default precision, you must provide a positive value
        for this parameter (because negative precisions are undefined and can cause errors in this function's
        logarithmic operations).

    Returns
    -------
    num_leading_zeros : int
        The number of leading zeros in the float value (up to the specified precision).

    Raises
    ------
    TypeError
        Raised if the value to round or the precision is not a float or integer.
    ValueError
        Raised if the precision is not positive and is not the default value of -1.
    """
    error_lib.check_type(float_val, float, "float value", alt_type=int)
    if prec != -1:
        error_lib.check_type(prec, float, "float precision", alt_type=int)
        error_lib.check_value_is_positive(prec, "float precision")
    num_leading_zeros = 0
    abs_float_val = abs(float_val)
    if abs_float_val < 1.0:
        num_multiplies = 0
        max_num_multiplies = 15
        if prec != -1:
            max_num_multiplies = int(-m.log10(prec))
        temp_val = abs_float_val
        while temp_val < 1 and num_multiplies < max_num_multiplies:
            temp_val *= 10.0
            num_multiplies += 1
        num_leading_zeros = num_multiplies - 1
    return num_leading_zeros

def get_num_sig_figs(val, prec):
    """Calculates the number of significant figures in an integer or float based on a specified precision.

    Parameters
    ----------
    val : int | float
        The value in which we should find the number of significant figures.
    prec : int | float
        The precision (base-10 order of magnitude at which we can measure the integer or float value) that should be
        used for calculating the number of significant figures. This value must be positive. A precision of 1 means
        we will count significant figures down to the ones place, 0.1 if we will count down to the tenths
        place, 0.01 if we will count down to the hundredths place, etc.

    Returns
    -------
    num_sig_figs : int
        The number of significant figures in the integer or float value.
    """
    error_lib.check_type(val, float, "val", alt_type=int)
    error_lib.check_type(prec, float, "precision", alt_type=int)
    error_lib.check_value_is_positive(prec, "precision")
    num_sig_figs = 0
    num_integer_digits = find_num_integer_digits(val)
    num_int_sig_figs = 0
    if prec <= 1:
        num_int_sig_figs = num_integer_digits
    else:
        num_int_sig_figs = num_integer_digits - int(m.log10(prec))
    num_float_sig_figs = 0
    if prec < 1:
        num_float_sig_figs = int(-1 * m.log10(prec))
    if num_int_sig_figs == 0:
        num_leading_zeros = get_num_leading_decimal_zeros(val, prec)
        num_sig_figs = num_float_sig_figs - num_leading_zeros
    else:
        num_sig_figs = num_int_sig_figs + num_float_sig_figs
    return num_sig_figs

def add_vals_with_sig_figs(val_1, val_2, val_1_prec=-1, val_2_prec=-1):
    """Calculates the sum of two values rounded to the correct number of significant figures.

    Parameters
    ----------
    val_1 : int | float
        The first value in the sum.
    val_2 : int | float
        The second value in the sum.
    val_1_prec : int | float, default -1
        The precision of the first value (1 for value rounded to the ones place, 10 for value rounded to the tens
        0.1 for value round to the tenths place, etc.). If the first value is a constant with an infinite precision,
        please use the default precision of -1.
    val_2_prec : int | float, default -1
        The precision of the second value (1 for value rounded to the ones place, 10 for value rounded to the tens
        0.1 for value round to the tenths place, etc.). If the second value is a constant with an infinite precision,
        please use the default precision of -1.

    Returns
    -------
    rounded_sum : int | float
        The sum of two values rounded to the correct number of significant figures.
    num_sig_figs : int
        The number of significant figures in the sum value. If the sum is a constant with an infinite precision,
        this value will be -1 (because a constant theoretically has infinitely many significant figures).
    """
    error_lib.check_type(val_1, float, "Value 1 (in add with sig figs)", alt_type=int)
    error_lib.check_type(val_2, float, "Value 2 (in add with sig figs)", alt_type=int)
    error_lib.check_type(val_1_prec, float, "Value 1 Precision (in add with sig figs)", alt_type=int)
    if val_1_prec != -1:
        error_lib.check_value_is_positive(val_1_prec, "Value 1 Precision")
    error_lib.check_type(val_2_prec, float, "Value 2 Precision (in add with sig figs)", alt_type=int)
    if val_2_prec != -1:
        error_lib.check_value_is_positive(val_2_prec, "Value 2 Precision")
    unrounded_result = val_1 + val_2
    rounded_sum = unrounded_result
    num_sig_figs = -1
    if val_1_prec != -1 or val_2_prec != -1:
        bigger_prec = val_1_prec
        if val_1_prec == -1:
            bigger_prec = val_2_prec
        if val_1_prec != -1 and val_2_prec != -1:
            if val_1_prec > val_2_prec:
                bigger_prec = val_1_prec
            else:
                bigger_prec = val_2_prec
        rounded_sum = round_to_precision(unrounded_result, bigger_prec)
        num_sig_figs = get_num_sig_figs(unrounded_result, bigger_prec)
    return rounded_sum, num_sig_figs

def add_list_vals_with_sig_figs(val_list, precisions=-1):
    """Calculates the sum of all values in a list rounded to the correct number of significant figures.

    Parameters
    ----------
    val_list : list[int | float]
        The list of values to sum.
    precisions : int | float | list[int | float], default -1
        The precisions of the list values (e.g., -1 for infinite precision, 10 for value rounded to the tens, 1 for
        value rounded to the ones place, 0.1 for value rounded to the tenths place, etc.). If a single precision value
        is provided, this precision will be applied to all of the list values. If the list contains values with
        different precisions, provide the different values in the form of a list. The order of the precisions does
        not matter, because the largest precision value will always be the one that is ultimately used for rounding
        the sum result.

    Returns
    -------
    rounded_sum : int | float
        The sum of the list values rounded to the correct number of significant figures.
    num_sig_figs : int
        The number of significant figures in the sum value. If the sum is a constant with an infinite precision,
        this value will be -1 (because a constant theoretically has infinitely many significant figures).
    """
    error_lib.check_type(val_list, list, "Value List (in add list values with sig figs)")
    error_lib.check_type(precisions, list, "Value Precisions (in add list values with sig figs)",
                         alt_types=[int, float])
    unrounded_result = sum(val_list)
    result_prec = -1
    if type(precisions) == int or type(precisions) == float:
        result_prec = precisions
    else:
        result_prec = max(precisions)
    rounded_sum = unrounded_result
    num_sig_figs = -1
    if result_prec != -1:
        rounded_sum = round_to_precision(unrounded_result, result_prec)
        num_sig_figs = get_num_sig_figs(unrounded_result, result_prec)
    return rounded_sum, num_sig_figs

def mult_vals_with_sig_figs(val_1, val_2, val_1_prec=-1, val_2_prec=-1):
    """Calculates the product of two values rounded to the correct number of significant figures.

    Parameters
    ----------
    val_1 : int | float
        The first value in the product.
    val_2 : int | float
        The second value in the product.
    val_1_prec : int | float, default -1
        The precision of the first value (1 for value rounded to the ones place, 10 for value rounded to the tens
        0.1 for value round to the tenths place, etc.). If the first value is a constant with an infinite precision,
        please use the default precision of -1.
    val_2_prec : int | float, default -1
        The precision of the second value (1 for value rounded to the ones place, 10 for value rounded to the tens
        0.1 for value round to the tenths place, etc.). If the second value is a constant with an infinite precision,
        please use the default precision of -1.

    Returns
    -------
    rounded_prod : int | float
        The product of two values rounded to the correct number of significant figures.
    num_sig_figs : int
        The number of significant figures in the product value. If the product is a constant with an infinite precision,
        this value will be -1 (because a constant theoretically has infinitely many significant figures).
    """
    error_lib.check_type(val_1, float, "Value 1 (in mult with sig figs)", alt_type=int)
    error_lib.check_type(val_2, float, "Value 2 (in mult with sig figs)", alt_type=int)
    error_lib.check_type(val_1_prec, float, "Value 1 Precision (in mult with sig figs)", alt_type=int)
    if val_1_prec != -1:
        error_lib.check_value_is_positive(val_1_prec, "Value 1 Precision (in mult with sig figs)")
    error_lib.check_type(val_2_prec, float, "Value 2 Precision (in mult with sig figs)", alt_type=int)
    if val_2_prec != -1:
        error_lib.check_value_is_positive(val_2_prec, "Value 2 Precision (in mult with sig figs)")
    unrounded_result = val_1 * val_2
    rounded_prod = unrounded_result
    val_1_num_sig_figs = -1
    if val_1_prec != -1:
        val_1_num_sig_figs = get_num_sig_figs(val_1, val_1_prec)
    val_2_num_sig_figs = -1
    if val_2_prec != -1:
        val_2_num_sig_figs = get_num_sig_figs(val_2, val_2_prec)
    num_prod_sig_figs = -1
    if val_1_prec != -1 and val_2_prec != -1:
        num_prod_sig_figs = val_1_num_sig_figs
        if val_2_num_sig_figs < val_1_num_sig_figs:
            num_prod_sig_figs = val_2_num_sig_figs
    elif val_1_prec != -1 and val_2_prec == -1:
        num_prod_sig_figs = val_1_num_sig_figs
    elif val_1_prec == -1 and val_2_prec != -1:
        num_prod_sig_figs = val_2_num_sig_figs
    if num_prod_sig_figs != -1:
        rounded_prod = round_to_num_sig_figs(unrounded_result, num_prod_sig_figs)
    return rounded_prod, num_prod_sig_figs

def convert_deg_to_rad_with_sig_figs(num_degrees, prec=-1):
    """Converts an angle in degrees to the equivalent number of radians (rounded to the correct number of significant
    figures).

    Parameters
    ----------
    num_degrees : int | float
        The angle in degrees.
    prec : int | float, default -1
        The precision of the angle measured in degrees (-1 if it is infinitely precise, 10 if it is known to the tens
        place, 1 if it is known to the ones place, 0.1 if it is known to the tenths, etc.).

    Returns
    -------
    rounded_num_rads : float
        The angle in radians rounded to the correct number of significant figures.
    num_rad_sig_figs : int
        The number of significant figures in the radian angle value.
    """
    error_lib.check_type(num_degrees, float, "Angle Size in Degrees", alt_type=float)
    error_lib.check_type(prec, int, "Degree Angle Size Precision", alt_type=float)
    if prec != -1:
        error_lib.check_value_is_positive(prec, "Degree Angle Size Precision")
    unrounded_num_rads = (2.0 * PI / 360.0) * num_degrees
    rounded_num_rads = unrounded_num_rads
    num_rad_sig_figs = -1
    if prec != -1:
        num_deg_sig_figs = get_num_sig_figs(num_degrees, prec)
        num_rad_sig_figs = num_deg_sig_figs
        rounded_num_rads = round_to_num_sig_figs(unrounded_num_rads, num_rad_sig_figs)
    return rounded_num_rads, num_rad_sig_figs






def rect_area(length, width, length_prec=-1, width_prec=-1):
    error_lib.check_type(length, float, "length", alt_type=int)
    error_lib.check_value_is_positive_or_zero(length, "length")
    error_lib.check_type(width, float, "width", alt_type=int)
    error_lib.check_value_is_positive_or_zero(width, "width")
    error_lib.check_type(length_prec, float, "length precision", alt_type=int)
    if length_prec != -1:
        error_lib.check_value_is_positive(length_prec, "length precision")
    error_lib.check_type(width_prec, float, "width precision", alt_type=int)
    if length_prec != -1:
        error_lib.check_value_is_positive(length_prec, "width precision")
    rect_area, rect_area_num_sig_figs = mult_vals_with_sig_figs(length, width, length_prec, width_prec)
    return rect_area, rect_area_num_sig_figs

def square_area(side_length, side_length_prec=-1):
    error_lib.check_type(side_length, float, "side length", alt_type=int)
    error_lib.check_value_is_positive_or_zero(side_length, "side length")
    error_lib.check_type(side_length_prec, float, "side length precision", alt_type=int)
    if side_length_prec != -1:
        error_lib.check_value_is_positive(side_length_prec, "side length precision")
    square_area, square_area_num_sig_figs = rect_area(side_length, side_length, side_length_prec, side_length_prec)
    return square_area, square_area_num_sig_figs

