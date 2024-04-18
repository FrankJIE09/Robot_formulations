import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 定义机器人的运动学模型
def forward_kinematics(theta1, theta2):
    # 两轴机器人的简化运动学模型
    x = np.cos(theta1) + np.cos(theta1 + theta2)
    y = np.sin(theta1) + np.sin(theta1 + theta2)
    z = 0  # 二维平面上的运动

    return x, y, z


# 定义雅可比矩阵
def jacobian(theta1, theta2):
    # 对于这个简化模型，雅可比矩阵可以直接计算
    J = np.array([[-np.sin(theta1) - np.sin(theta1 + theta2), -np.sin(theta1 + theta2)],
                  [np.cos(theta1) + np.cos(theta1 + theta2), np.cos(theta1 + theta2)],
                  [0, 0]])

    return J


# 计算速度椭球的参数
theta1_range = np.linspace(0, 2 * np.pi, 50)
theta2_range = np.linspace(0, 2 * np.pi, 50)
v_ellipse_params = []

for theta1 in theta1_range:
    for theta2 in theta2_range:
        J = jacobian(theta1, theta2)
        # 计算特征值和特征向量
        eigenvalues, eigenvectors = np.linalg.eig(J @ J.T)
        # 计算速度椭球的半长轴和半短轴
        a = np.sqrt(eigenvalues[0])
        b = np.sqrt(eigenvalues[1])
        v_ellipse_params.append((a, b))

# 绘制速度椭球
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for a, b in v_ellipse_params:
    u = np.linspace(0, 2 * np.pi, 100)
    x = a * np.cos(u)
    y = b * np.sin(u)
    z = np.zeros_like(u)
    ax.plot(x, y, z, color='b')
    # plt.show()

ax.set_xlabel('X Velocity')
ax.set_ylabel('Y Velocity')
ax.set_zlabel('Z Velocity')
ax.set_title('Velocity Capability Ellipsoid')

plt.show()
