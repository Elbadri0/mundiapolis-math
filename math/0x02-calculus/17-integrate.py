#!/usr/bin/env python3
'''Calculates the integral of a polynomial.
'''


def poly_integral(poly, C=0):
    '''Calculates the integral of a polynomial.

    Args:
        poly: List of coefficients representing a polynomial.
        C: Integer representing the integration constant.

    Returns:
        List of coefficients representing the integral of the polynomial.
        If poly or C are not valid, return None.
    '''

    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if not isinstance(C, (int, float)):
        return None
    if isinstance(C, int):
        C = int(C)
    integral = [C]
    if poly == [0]:
        return integral
    for idx, x in enumerate(poly):
        if not isinstance(x, (int, float)):
            return None
        res = x / (idx + 1)
        if res.is_integer():
            res = int(res)
        integral.insert(idx + 1, res)
    return integral
