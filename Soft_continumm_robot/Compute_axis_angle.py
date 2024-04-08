# Author: Frank & Chatgpt
# Edit Date: 2024-04-08
# Code Purpose: Compute axis-angle representation from a given rotation matrix
import numpy as np
from scipy.spatial.transform import Rotation

# 假设你有一个3x3的旋转矩阵
rotation_matrix = Rotation.as_matrix(Rotation.from_euler('xyz', [np.pi, 0, 0]))

# 计算旋转角度
theta = np.arccos((np.trace(rotation_matrix) - 1) / 2)

# 计算旋转轴
axis = 1 / (2 * np.sin(theta)) * np.array([rotation_matrix[2, 1] - rotation_matrix[1, 2],
                                           rotation_matrix[0, 2] - rotation_matrix[2, 0],
                                           rotation_matrix[1, 0] - rotation_matrix[0, 1]])

# 输出轴角向量
print("Axis-Angle Vector:", axis * theta)
print("theta:", theta)
