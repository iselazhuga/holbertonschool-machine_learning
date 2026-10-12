#!/usr/bin/env python3
"""A script that sorts a pd.DataFrame by High in descending order"""


def high(df):
    """Returns df sorted by the High column, highest first"""
    return df.sort_values(by="High", ascending=False)
