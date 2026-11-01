#!/usr/bin/env python3
"""Binomial distribution."""


class Binomial:
    """Represent a binomial distribution."""

    def __init__(self, data=None, n=1, p=0.5):
        """Initialize the distribution from data or from given n and p.

        With data, n and p are estimated by the method of moments:
        p = 1 - variance / mean, n = round(mean / p), then p = mean / n.
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            p = 1 - variance / mean
            self.n = round(mean / p)
            self.p = float(mean / self.n)

    @staticmethod
    def factorial(x):
        """Return x! for a non-negative integer x."""
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result

    def pmf(self, k):
        """Return the probability of exactly k successes in n trials.

        k is turned into an integer; a k below 0 or above n gives 0.
        """
        k = int(k)
        if k < 0 or k > self.n:
            return 0
        fact = self.factorial
        comb = fact(self.n) // (fact(k) * fact(self.n - k))
        return comb * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """Return the probability of at most k successes in n trials.

        Adds the probabilities of 0, 1, ..., k successes. k is turned
        into an integer; a negative k gives 0.
        """
        k = int(k)
        if k < 0:
            return 0
        fact = self.factorial
        q = 1 - self.p
        total = 0
        for i in range(0, min(k, self.n) + 1):
            total += (fact(self.n) * (self.p ** i) * (q ** (self.n - i))
                      / (fact(i) * fact(self.n - i)))
        return total
