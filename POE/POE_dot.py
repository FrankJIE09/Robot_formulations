import numpy as np
import sympy as sp


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
    R = np.eye(3) + sp.sin(theta) * omega_hat + (1 - sp.cos(theta)) * np.dot(omega_hat, omega_hat)
    return R


def exp_map_v(w, v, theta):
    """
    计算线速度向量 v 的指数映射
    """
    omega_hat = skew_symmetric(w)

    return (np.eye(3) * theta + (1 - sp.cos(theta)) * omega_hat +
            (theta - sp.sin(theta)) * np.dot(omega_hat, omega_hat)) @ v


def POE(omega, v, theta):
    # 定义旋转轴和线速度

    R = exp_map_omega(omega, theta)  # 旋转变换
    P = exp_map_v(omega, v, theta)  # 平移变换
    T = sp.eye(4)
    T[:3, :3] = R
    T[:3, -1] = P
    # print("指数积的转换矩阵：")
    # print(T)
    return T

if __name__ == '__main__':

    M = np.eye(4)
    M[2, -1] = 1

    omega1 = np.array([0, 0, 1])  # 旋转轴（单位向量）
    v1 = np.array([0, 0, 0])  # 线速度方向
    theta1 = np.radians(0)

    omega2 = np.array([0, 0, 1])  # 旋转轴（单位向量）
    v2 = np.array([1, 0, 0])  # 线速度方向
    theta2 = np.radians(90)

    omega3 = np.array([0, 0, 1])  # 旋转轴（单位向量）
    v3 = np.array([2, 0, 0])  # 线速度方向
    theta3 = np.radians(-90)

    omega4 = np.array([0, 0, 0])  # 旋转轴（单位向量）
    v4 = np.array([0, 0, 1])  # 线速度方向
    theta4 = 10
    T1 = POE(omega1, v1, theta1)
    T2 = POE(omega2, v2, theta2)
    T3 = POE(omega3, v3, theta3)
    T4 = POE(omega4, v4, theta4)
    print(T1 @ T2 @ T3 @ T4 @ M)
