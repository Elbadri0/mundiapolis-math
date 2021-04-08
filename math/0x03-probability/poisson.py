#!/usr/bin/env python3
'''Module with Poisson class.
'''


class Poisson():
    '''Represents a Poisson distribution.
    '''

    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        '''Initialize class.

        Args:
            data:
                List of the data to be used to estimate the distribution.
            lambtha:
                Expected number of occurences in a given time frame.
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
            else:
                self.lambtha = float(sum(data) / len(data))

    def factorial(self, k):
        '''Calculates the factorial of a given number

        k:
            Integer.

        Returns:
            Factorial of k.
        '''

        if k == 0:
            return 1
        else:
            return k * self.factorial(k - 1)

    def pmf(self, k):
        '''Calculates the value of the PMF for a given number of “successes”.

        Args:
            k:
                Number of successes
        '''

        if not isinstance(k, int):
            k = int(k)
        if k <= 0:
            return 0
        return (((self.lambtha**k) * (self.e ** (self.lambtha * -1)))
                / self.factorial(k))

    def cdf(self, k):
        '''Calculates the value of the CDF for a given number of “successes”.

        Args:
            k:
                Number of successes
        '''

        if not isinstance(k, int):
            k = int(k)
        if k <= 0:
            return 0
        cdf = 0
        for j in range(0, k + 1):
            cdf += (((self.e ** (self.lambtha * -1)) * (self.lambtha ** j))
                    / self.factorial(j))
        return cdf
