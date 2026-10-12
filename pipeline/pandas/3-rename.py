#!/usr/bin/env python3
"""A script that renames and converts the Timestamp column of a pd.DataFrame"""
import pandas as pd


def rename(df):
    """Renames Timestamp to Datetime, converts it to datetime,
    and keeps only the Datetime and Close columns"""
    df = df.rename(columns={"Timestamp": "Datetime"})
    df["Datetime"] = pd.to_datetime(df["Datetime"], unit="s")
    return df[["Datetime", "Close"]]
