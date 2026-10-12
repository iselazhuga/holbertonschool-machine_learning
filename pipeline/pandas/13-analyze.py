#!/usr/bin/env python3
"""A script that computes descriptive statistics of a pd.DataFrame"""


def analyze(df):
    """Returns descriptive statistics for all columns except Timestamp"""
    return df.drop(columns=["Timestamp"]).describe()
