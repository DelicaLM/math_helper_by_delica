import error_helper_by_delica as error_lib


def round_to_prec(val, prec):
    error_lib.check_type(val, float, "value to round", alt_type=int)
    result = val
    if prec != -1:
        error_lib.check_type(prec, float, "precision", alt_type=int)

    return result


def add_vals_with_sig_figs(val_1, val_2, prec_1=-1, prec_2=-1):
    result = val_1 + val_2
    result_pres = -1

