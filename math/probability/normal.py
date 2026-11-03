#!/usr/bin/env python3
"""Normal distribution."""


class Normal:
    """Represent a normal distribution."""

    e = 2.7182818285
    pi = 3.1415926536

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initialize the distribution from data or from mean and stddev.

        If data is given, mean and stddev are the mean and the population
        standard deviation of the data.
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            total = 0
            for x in data:
                total += x
            self.mean = float(total / len(data))
            squares = 0
            for x in data:
                squares += (x - self.mean) ** 2
            self.stddev = float((squares / len(data)) ** 0.5)

    def z_score(self, x):
        """Return how many standard deviations x is from the mean."""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Return the value that is z standard deviations from the mean."""
        return self.mean + z * self.stddev

    def pdf(self, x):
        """Return the height of the bell curve at x."""
        coefficient = 1 / (self.stddev * (2 * self.pi) ** 0.5)
        exponent = -0.5 * ((x - self.mean) / self.stddev) ** 2
        return coefficient * self.e ** exponent

    def erf(self, v):
        """Return the error function of v, from its Taylor series."""
        series = v - v ** 3 / 3 + v ** 5 / 10 - v ** 7 / 42 + v ** 9 / 216
        return (2 / self.pi ** 0.5) * series

    def cdf(self, x):
        """Return the probability that a value is at most x."""
        v = (x - self.mean) / (self.stddev * 2 ** 0.5)
        return 0.5 * (1 + self.erf(v))
