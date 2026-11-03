#!/usr/bin/env python3
"""Normal distribution."""


class Normal:
    """Represent a normal distribution."""

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
