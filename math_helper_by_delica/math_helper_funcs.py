import error_helper_by_delica as error_lib


def round_to_precision(val, prec):
    result = val
    if prec != -1:
        error_lib.check_type(val, float, "value to round", alt_type=int)
        error_lib.check_value_is_positive(prec, "rounding precision")
    return val
