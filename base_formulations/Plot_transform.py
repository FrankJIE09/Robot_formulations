import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 定义旋转矩阵的函数
def rotation_matrix_x(theta):
    return np.array([[1, 0, 0],
                     [0, np.cos(theta), -np.sin(theta)],
                     [0, np.sin(theta), np.cos(theta)]])


def rotation_matrix_y(theta):
    return np.array([[np.cos(theta), 0, np.sin(theta)],
                     [0, 1, 0],
                     [-np.sin(theta), 0, np.cos(theta)]])


def rotation_matrix_z(theta):
    return np.array([[np.cos(theta), -np.sin(theta), 0],
                     [np.sin(theta), np.cos(theta), 0],
                     [0, 0, 1]])


# 计算从s到b的变换矩阵
theta_x = np.radians(90)
theta_y = np.radians(90)
theta_z = np.radians(0)

T_s_to_b = rotation_matrix_x(theta_x) @ rotation_matrix_y(theta_y) @ rotation_matrix_z(theta_z)

point_s = np.array([0.1, 0.2, 0.3])

# 将点从s坐标系变换到b坐标系
point_b = T_s_to_b.T @ point_s

# 绘制坐标系转换过程
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制s坐标系
ax.quiver(0, 0, 0, 1, 0, 0, color='r', arrow_length_ratio=0.3)
ax.quiver(0, 0, 0, 0, 1, 0, color='g', arrow_length_ratio=0.3)
ax.quiver(0, 0, 0, 0, 0, 1, color='b', arrow_length_ratio=0.3)

# 绘制b坐标系
ax.quiver(0, 0, 0, T_s_to_b[0, 0], T_s_to_b[1, 0], T_s_to_b[2, 0], color='r', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, T_s_to_b[0, 1], T_s_to_b[1, 1], T_s_to_b[2, 1], color='g', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, T_s_to_b[0, 2], T_s_to_b[1, 2], T_s_to_b[2, 2], color='b', arrow_length_ratio=0.1)

# 绘制原点变换前后的点
ax.scatter(point_s[0], point_s[1], point_s[2], color='k', label='Point in s')
ax.scatter(point_b[0], point_b[1], point_b[2], color='m', label='Point in b')

# 设置坐标轴
# 设置坐标轴范围
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.title('Coordinate Transformation')
plt.legend()
plt.show()
