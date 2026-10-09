#!/usr/bin/env python3
"""A script that creates a pd.DataFrame from a np.ndarray"""

import pandas as pd


def from_numpy(array):
    """A function that creates a pd.DataFrame from a np.ndarray"""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num_columns = array.shape[1]
    column_names = list(letters[:num_columns])
    df = pd.DataFrame(array, columns=column_names)
    return df
