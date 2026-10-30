#!/usr/bin/env python3
"""Poisson distribution."""


class Poisson:
    """Represent a Poisson distribution."""

    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        """Initialize the distribution from data or from a given lambtha.

        If data is given, lambtha is the mean of the data.
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
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """Return the probability of exactly k successes.

        k is turned into an integer; a negative k gives 0.
        """
        k = int(k)
        if k < 0:
            return 0
        factorial = 1
        for i in range(1, k + 1):
            factorial *= i
        return (self.e ** -self.lambtha) * (self.lambtha ** k) / factorial
