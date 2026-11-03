#!/usr/bin/env python3
"""Exponential distribution."""


class Exponential:
    """Represent an exponential distribution."""

    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        """Initialize the distribution from data or from a given lambtha.

        If data is given, lambtha is 1 divided by the mean of the data.
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            total = 0
            for x in data:
                total += x
            self.lambtha = float(len(data) / total)

    def pdf(self, x):
        """Return the density of the distribution at time x.

        A negative x gives 0.
        """
        if x < 0:
            return 0
        return self.lambtha * self.e ** (-self.lambtha * x)

    def cdf(self, x):
        """Return the probability that the event happens within time x.

        A negative x gives 0.
        """
        if x < 0:
            return 0
        return 1 - self.e ** (-self.lambtha * x)
