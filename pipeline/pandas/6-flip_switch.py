#!/usr/bin/env python3
"""A script that sorts a pd.DataFrame in reverse order and transposes it"""


def flip_switch(df):
    """Sorts df in reverse chronological order and returns its transpose"""
    return df.sort_index(ascending=False).T
