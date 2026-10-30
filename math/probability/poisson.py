#!/usr/bin/env python3
"""Poisson distribution."""


class Poisson:
    """Represent a Poisson distribution."""

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
