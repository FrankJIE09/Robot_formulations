import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_spiral_axis(s, q, h, num_turns=5, num_points_per_turn=100):
    t = np.linspace(0, 2 * np.pi * num_turns, num_points_per_turn * num_turns)
    x = q[0] + h * np.cos(t) + s[0] * t
    y = q[1] + h * np.sin(t) + s[1] * t
    z = q[2] + s[2] * t
    return x, y, z


# Define parameters
q = np.array([3, 0, 0])  # 轴线上一点
s = np.array([0, 0, 1])  # 轴的方向
h = 2  # 螺距

# 绘制螺旋轴
x, y, z = plot_spiral_axis(s, q, h)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
