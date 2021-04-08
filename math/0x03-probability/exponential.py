#!/usr/bin/env python3
'''Exponential class module
'''


class Exponential():
    '''Represents an exponential distribution
    '''

    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        '''Contstructor for class Exponential.

        Args:
            data: List of data to be used to estimate the distribution.
            lambtha: Expected number of occurences in a given time frame.
        '''

        if data is None:
            if lambtha <= 0:
                raise ValueError('lambtha must be a positive value')
            else:
                self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.lambtha = float(1 / (sum(data) / len(data)))

    def pdf(self, x):
        '''Calculates the value of the PDF for a given number of “successes”.

        Args:
            x:
                Number of successes
        '''

        if x < 0:
            return 0
        return self.lambtha * (self.e ** ((-1) * self.lambtha * x))

    def cdf(self, x):
        '''Calculates the value of the CDF for a given number of “successes”.

        Args:
            x:
                Number of successes
        '''

        if x < 0:
            return 0
        return 1 - (self.e ** ((-1 * self.lambtha) * x))
