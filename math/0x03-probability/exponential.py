#!/usr/bin/env python3
'''Exponential class
'''


class Exponential():
    '''exponential distribution
    '''

    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        '''class Exponential
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
        '''Calculates the value of the PDF
        '''

        if x < 0:
            return 0
        return self.lambtha * (self.e ** ((-1) * self.lambtha * x))

    def cdf(self, x):
        '''Calculates the value of the CDF
        '''

        if x < 0:
            return 0
        return 1 - (self.e ** ((-1 * self.lambtha) * x))
