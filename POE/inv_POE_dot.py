import numpy as np
from base_formulations.adjoint_matrix import adjoint_transform


def skew_symmetric(w):
    """
    计算旋转向量 w 的反对称矩阵
    """
    return np.array([[0, -w[2], w[1]],
                     [w[2], 0, -w[0]],
                     [-w[1], w[0], 0]])


def exp_map_omega(w, theta):
    """
    计算旋转向量 w 的指数映射
    """
    omega_hat = skew_symmetric(w)
    R = np.eye(3) + np.sin(theta) * omega_hat + (1 - np.cos(theta)) * np.dot(omega_hat, omega_hat)
    return R


def exp_map_v(w, v, theta):
    """
    计算线速度向量 v 的指数映射
    """
    omega_hat = skew_symmetric(w)

    return (np.eye(3) * theta + (1 - np.cos(theta)) * omega_hat +
            (theta - np.sin(theta)) * np.dot(omega_hat, omega_hat)) @ v


def inv_POE(omega, v, theta):
    # 定义旋转轴和线速度

    R = exp_map_omega(omega, theta)  # 旋转变换
    P = exp_map_v(omega, v, theta)  # 平移变换
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, -1] = P
    print("指数积的转换矩阵：")
    print(T)
    return T


def error_inv_POE(omega, v, theta):
    # 定义旋转轴和线速度

    S = np.zeros((4, 4))
    S[:3, :3] = skew_symmetric(omega)
    S[:3, -1] = v
    print(S)

    AdT_M = adjoint_transform(np.linalg.inv(M))

    B = AdT_M @ np.concatenate((omega, v))
    B_omega = B[:3]
    B_v = B[3:]
    R = exp_map_omega(B_omega, theta)  # 旋转变换
    P = exp_map_v(B_omega, B_v, theta)  # 平移变换
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, -1] = P
    print("指数积的转换矩阵：")
    print(T)
    return T


M = np.eye(4)
M[2, -1] = 1

omega1 = np.array([0, 0, 1])  # 旋转轴（单位向量）
v1 = np.array([-2, 0, 0])  # 线速度方向
theta1 = np.radians(0)

omega2 = np.array([0, 0, 1])  # 旋转轴（单位向量）
v2 = np.array([-1, 0, 0])  # 线速度方向
theta2 = np.radians(90)

omega3 = np.array([0, 0, 1])  # 旋转轴（单位向量）
v3 = np.array([0, 0, 0])  # 线速度方向
theta3 = np.radians(-90)

omega4 = np.array([0, 0, 0])  # 旋转轴（单位向量）
v4 = np.array([0, 0, 1])  # 线速度方向
theta4 = np.radians(0)
T1 = inv_POE(omega1, v1, theta1)
T2 = inv_POE(omega2, v2, theta2)
T3 = inv_POE(omega3, v3, theta3)
T4 = inv_POE(omega4, v4, theta4)
print(M @ T1 @ T2 @ T3 @ T4)
'''
M = np.eye(4)
M[2, -1] = 0.06 + 0.4 + 0.55
L1 = 0.55
L2 = 0.3
L3 = 0.06
W1 = 0.045
omega2 = np.array([0, 1, 0])  # 旋转轴（单位向量）
v2 = np.array([L1 + L2 + L3, 0, 0])  # 线速度方向
theta2 = np.radians(45)

omega4 = np.array([0, 1, 0])  # 旋转轴（单位向量）
v4 = np.array([L2 + L3, 0, W1])  # 线速度方向
theta4 = np.radians(-45)

omega6 = np.array([0, 1, 0])  # 旋转轴（单位向量）
v6 = np.array([L3, 0, 0])  # 线速度方向
theta6 = np.radians(-90)
T2 = inv_POE(omega2, v2, theta2)
T4 = inv_POE(omega4, v4, theta4)
T6 = inv_POE(omega6, v6, theta6)
print(M @ T2 @ T4 @ T6)


'''
