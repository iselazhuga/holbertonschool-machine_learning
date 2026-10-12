#!/usr/bin/env python3
"""A script that slices High, Low, Close and Volume_(BTC) every 60th row"""


def slice(df):
    """Returns every 60th row of High, Low, Close and Volume_(BTC)"""
    return df[["High", "Low", "Close", "Volume_(BTC)"]].iloc[::60]
