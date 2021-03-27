#!/usr/bin/env python3
'''Calculates the derivate of a polynomial.
'''


def poly_derivative(poly):
    '''Calculates the derivate of a polynomial.

    Args:
        poly: ist of coefficients representing a polynomial.
    '''

    if not isinstance(poly, list) or len(poly) == 0:
        return None
    derivate = []
    for idx, x in enumerate(poly):
        if idx - 1 < 0:
            pass
        else:
            derivate.insert(idx - 1, idx * x)
    if len(derivate) == 0:
        return [0]
    else:
        return derivate
