#!/usr/bin/env python3
"""A script that removes rows where Close is NaN from a pd.DataFrame"""


def prune(df):
    """Returns df without the rows where Close has NaN values"""
    return df.dropna(subset=["Close"])
