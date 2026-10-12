#!/usr/bin/env python3
"""A script that selects the last 10 rows of High and Close as a np.ndarray"""


def array(df):
    """Returns the last 10 rows of High and Close as a numpy.ndarray"""
    return df[["High", "Close"]].tail(10).to_numpy()
