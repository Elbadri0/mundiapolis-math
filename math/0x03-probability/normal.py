#!/usr/bin/env python3
'''Normal distribution
'''


class Normal():
    '''Class of Normal distribution
    '''

    e = 2.7182818285
    pi = 3.1415926536

    def __init__(self, data=None, mean=0., stddev=1.):
        '''Normal class
        '''

        if data is None:
            self.mean = float(mean)
            if stddev <= 0:
                raise ValueError('stddev must be a positive value')
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.mean = float(sum(data) / len(data))
            variance = 0
            for point in data:
                variance += (self.mean - point) ** 2
            self.stddev = float((variance / len(data)) ** 0.5)

    def factorial(self, k):
        '''Calculates the factorial
        '''

        if k == 0:
            return 1
        else:
            return k * self.factorial(k - 1)

    def z_score(self, x):
        '''Calculates the z-score
        '''

        return float((x - self.mean) / self.stddev)

    def x_value(self, z):
        '''Calculates the x-value
        '''

        return float((self.stddev * z) + self.mean)

    def pdf(self, x):
        '''Calculates the value of the PDF
        '''

        dividend = (self.e ** ((-1 * ((x - self.mean) ** 2))
                    / (2 * (self.stddev ** 2))))
        divisor = self.stddev * ((2 * self.pi) ** 0.5)
        return float(dividend / divisor)

    def cdf(self, x):
        '''Calculates the value of the CDF
        '''

        if x == 0:
            return float(1 / 2)
        sum = 0
        erf_x = (x - self.mean) / (self.stddev * (2 ** 0.5))
        for n in range(5):
            sum += (((-1) ** n) * (erf_x ** ((2 * n) + 1))
                    / (self.factorial(n) * ((2 * n) + 1)))
        erf = ((2 / (self.pi ** 0.5)) * sum)
        return (1 / 2) * (1 + erf)
