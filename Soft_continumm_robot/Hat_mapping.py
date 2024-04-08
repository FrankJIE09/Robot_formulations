# Author: Frank
# Edit Date: 2024-04-08
# Code Purpose: Hat mapping functions for so(3) and se(3)

import numpy as np

def hat_map_so3(v):
    """
    Maps a 3-dimensional vector v to the hat mapping result of so(3).
    """
    return np.array([[0, -v[2], v[1]],
                     [v[2], 0, -v[0]],
                     [-v[1], v[0], 0]])

def hat_map_se3(xi):
    """
    Maps a 6-dimensional vector xi to the hat mapping result of se(3).
    """
    v = xi[:3]
    w = xi[3:]
    return np.block([
        [hat_map_so3(w), v[:, np.newaxis]],
        [np.zeros(3), 0]
    ])

# Example vector
v = np.array([1, 2, 3])

# Compute the hat mapping result
hat_v = hat_map_so3(v)
print("Hat Mapping Result:")
print(hat_v)

# Example vector
xi = np.array([1, 2, 3, 0.1, 0.2, 0.3])

# Compute the hat mapping result
hat_xi = hat_map_se3(xi)
print("Hat Mapping Result:")
print(hat_xi)
