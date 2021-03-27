#!/usr/bin/env python3
'''
Calculates the sum of i to the power of 2 from i equals 1 to n.
'''


def summation_i_squared(n):
    '''
    Calculates the sum of i to the power of 2 from i equals 1 to n.
    '''

    if not isinstance(n, int) or n <= 0:
        return None
    return int((n*(n + 1)*(2*n + 1)) / 6)
