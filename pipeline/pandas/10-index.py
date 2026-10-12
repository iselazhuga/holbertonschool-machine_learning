#!/usr/bin/env python3
"""A script that sets the Timestamp column as the index of a pd.DataFrame"""


def index(df):
    """Returns df with Timestamp set as its index"""
    return df.set_index("Timestamp")
