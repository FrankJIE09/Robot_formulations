import numpy as np
import matplotlib.pyplot as plt

# 运动旋量的轴向量
omega = np.array([0, 2, 2])
# 线速度向量
v = np.array([4, 0, 0])

# 绘制轴向量
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, omega[0], omega[1], omega[2], color='r', label='Angular velocity')
ax.quiver(0, 0, 0, v[0], v[1], v[2], color='b', label='Linear velocity')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.legend()
plt.show()
