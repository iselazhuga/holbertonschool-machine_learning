#!/usr/bin/env python3
"""A script that builds a hierarchical index of bitstamp and coinbase data"""
import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """Concatenates bitstamp and coinbase rows in a 1417411980-1417417980 window"""
    df1 = index(df1)
    df2 = index(df2)
    low, high = 1417411980, 1417417980
    df1 = df1[(df1.index >= low) & (df1.index <= high)]
    df2 = df2[(df2.index >= low) & (df2.index <= high)]
    df = pd.concat([df2, df1], keys=["bitstamp", "coinbase"])
    df = df.swaplevel(0, 1).sort_index()
    return df
