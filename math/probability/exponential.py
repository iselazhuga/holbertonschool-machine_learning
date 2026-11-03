#!/usr/bin/env python3
"""Exponential distribution."""


class Exponential:
    """Represent an exponential distribution."""

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
