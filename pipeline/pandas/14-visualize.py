#!/usr/bin/env python3
"""A script that visualizes daily Bitcoin prices from 2017 onward"""

import matplotlib.pyplot as plt
import pandas as pd
from_file = __import__('2-from_file').from_file


def visualize(df):
    """Cleans, groups by day from 2017 and returns the transformed df"""
    df = df.drop(columns=["Weighted_Price"])
    df = df.rename(columns={"Timestamp": "Date"})
    df["Date"] = pd.to_datetime(df["Date"], unit="s")
    df = df.set_index("Date")
    df["Close"] = df["Close"].ffill()
    for col in ["High", "Low", "Open"]:
        df[col] = df[col].fillna(df["Close"])
    df["Volume_(BTC)"] = df["Volume_(BTC)"].fillna(0)
    df["Volume_(Currency)"] = df["Volume_(Currency)"].fillna(0)
    df = df.loc["2017":]
    df = df.groupby(pd.Grouper(freq="D")).agg({
        "High": "max",
        "Low": "min",
        "Open": "mean",
        "Close": "mean",
        "Volume_(BTC)": "sum",
        "Volume_(Currency)": "sum",
    })
    return df


df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
df = visualize(df)
print(df)
ax = df.plot(figsize=(12, 6), title="Bitcoin daily, 2017 onward")
ax.set_ylabel("")
plt.tight_layout()
plt.show()
