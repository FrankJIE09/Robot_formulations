import numpy as np
import sympy as sp
from POE.POE_dot import POE
from base_formulations.adjoint_matrix import adjoint_transform
from base_formulations.rodrigures import *


def compute_jacobian(axis_list, theta_list):
    assert len(axis_list) == len(theta_list), "轴数和角度数必须相同"
    axis_list = axis_list[::-1]
    theta_list = theta_list[::-1]
    J_list = []
    T_prev = np.eye(4)

    for axis, theta in zip(axis_list, theta_list):
        omega = np.array(axis)[:3]  # 提取旋转部分
        v = np.array(axis)[3:]  # 提取平移部分
        T = POE(omega, v, -theta)
        Ad_T = adjoint_transform(T_prev)
        B = np.hstack((omega, v))
        J = np.dot(Ad_T, B)
        J_list.append(sp.simplify(J))
        T_prev = np.dot(T_prev, T)

    return np.array(J_list[::-1]).T.astype(float)


def calculate_joint_velocity(Vd):
    np.set_printoptions(precision=4, suppress=True)

    L = 100

    omega1, omega2, omega3, = (0, 0, 1), (0, -1, 0), (0, -1, 0),
    v1, v2, v3, = (0, -2 * L, L), (0, 0, 2 * L), (0, 0, L),

    axis_list = [
        (omega1 + v1), (omega2 + v2), (omega3 + v3),
    ]
    theta_list = [0, 0, 0]

    J = compute_jacobian(axis_list, theta_list)
    print(J)
    theta_dot = np.linalg.pinv(J) @ Vd
    return theta_dot


# 示例调用
Vd = [10, 10, 10, 0, 0, 0]
theta_dot = calculate_joint_velocity(Vd)
print("关节速度：")
print(theta_dot)
