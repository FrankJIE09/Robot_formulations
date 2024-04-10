import numpy as np

# 给定多对对应的点坐标
P1 = np.array([[np.sqrt(2), 0, 2],
               [1, 1, -1],
               [0, 2 * np.sqrt(2), 0]]).T
P2 = np.array([[0, 2, np.sqrt(2)],
               [1 / np.sqrt(2), 1 / np.sqrt(2), -np.sqrt(2)],
               [-np.sqrt(2), np.sqrt(2), -2]]).T

# 计算旋转矩阵
R = np.dot(P2, np.linalg.inv(P1))

print("旋转矩阵 R：")
print(R)
