#!/usr/bin/env python3
"""Plots sampled elevations on a mountain as a colored scatter plot"""
import numpy as np
import matplotlib.pyplot as plt


def gradient():
    """Plots x and y as points colored by elevation z with a colorbar"""
    np.random.seed(5)

    x = np.random.randn(2000) * 10
    y = np.random.randn(2000) * 10
    z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))
    plt.figure(figsize=(6.4, 4.8))
    plt.scatter(x, y, c=z)
    plt.xlabel('x coordinate (m)')
    plt.ylabel('y coordinate (m)')
    plt.title('Mountain Elevation')
    cbar = plt.colorbar()
    cbar.set_label('elevation (m)')
    plt.show()
