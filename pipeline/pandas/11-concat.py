#!/usr/bin/env python3
"""A script that concatenates two pd.DataFrames indexed by Timestamp"""
import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    """Concatenates bitstamp rows up to 1417411920 above coinbase rows"""
    df1 = index(df1)
    df2 = index(df2)
    df2 = df2[df2.index <= 1417411920]
    return pd.concat([df2, df1], keys=["bitstamp", "coinbase"])
