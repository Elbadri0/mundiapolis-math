#!/usr/bin/env python3
'''Module for the binomial class.
'''


class Binomial():
    '''Representation of a binomial distribution.
    '''

    def __init__(self, data=None, n=1, p=0.5):
        '''Binomial class constructor.

        Args.
            data: List of the data to be used to estimate the distribution
            n: Number of Bernoulli trials
            p: Probability of a success
        '''

        if data is None:
            if n <= 0:
                raise ValueError('n must be a positive value')
            if p <= 0 or p >= 1:
                raise ValueError('p must be greater than 0 and less than 1')
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            mean = float(sum(data) / len(data))
            variance = float(sum([(x - mean) ** 2 for x in data]) / len(data))
            p = 1 - variance / mean
            self.n = round(mean / p)
            self.p = float(mean / self.n)

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
        '''Calculates the value of the PMF for a given number of “successes”

        Args.
            k: number of “successes”

        Returns.
            The PMF value for k
        '''

        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        n = self.n
        fac = self.factorial
        p = self.p
        nk = float(fac(n) / (fac(k) * fac(n - k)))
        return float(nk * ((p ** k) * ((1 - p) ** (n - k))))

    def cdf(self, k):
        '''Calculates the value of the CDF for a given number of “successes”

        Args.
            k: Number of "successes"

        Returns.
            The CDF value for k
        '''

        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)
        return cdf
