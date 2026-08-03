import math as m
import error_helper_by_delica as error_lib



def find_num_integer_digits(val):
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
                test = 0
            else:
                result = round(val, -prec_log)
                test = 0
    return result

result = round_to_precision(150.00, 10)
test = 0


def get_num_sig_figs(val, prec):
    test = 0

def rect_area(length, width, length_prec, width_prec):
    product = length * width
