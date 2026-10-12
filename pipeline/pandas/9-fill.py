#!/usr/bin/env python3
"""A script that cleans missing values in a pd.DataFrame of Bitcoin prices"""


def fill(df):
    """Fills missing values in Close, High, Low, Open and volume columns"""
    df = df.drop(columns=["Weighted_Price"])
    df["Close"] = df["Close"].ffill()
    for col in ["High", "Low", "Open"]:
        df[col] = df[col].fillna(df["Close"])
    df["Volume_(BTC)"] = df["Volume_(BTC)"].fillna(0)
    df["Volume_(Currency)"] = df["Volume_(Currency)"].fillna(0)
    return df
