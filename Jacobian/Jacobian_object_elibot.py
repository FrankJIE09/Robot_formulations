import time

import numpy as np
import sympy as sp
from POE.POE_dot import *
from base_formulations.adjoint_matrix import *
from base_formulations.rodrigures import *


def compute_jacobian(axis_list, theta_list, ):
    assert len(axis_list) == len(theta_list) #"轴数、角度数和长度数必须相同"
    axis_list = axis_list[::-1]
    theta_list = theta_list[::-1]
    J_list = []
    T_prev = np.eye(4)

    for axis, theta in zip(axis_list, theta_list):
        omega = np.array(axis)[0:3]
        v = np.array(axis)[3:]

        # 计算当前变换矩阵
        T = POE(omega, v, -theta)

        # 计算伴随变换矩阵Ad(T)
        Ad_T = adjoint_transform(T_prev)

        # 构造齐次变换矩阵的对数映射矩阵
        S = np.hstack((omega, v))

        # 计算雅可比矩阵
        J = np.dot(Ad_T, S)
        J_list.append(sp.simplify(J))

        # 更新T_prev
        T_prev = np.dot(T_prev, T)

    return (np.array(J_list[::-1]).T).astype(float)


if __name__ == '__main__':
    np.set_printoptions(precision=3, suppress=True)

    # 示例调用
    # theta1, theta2, theta3, theta4, theta5, theta6 = sp.symbols('theta1 theta2 theta3 theta4 theta5 theta6')
    # L1, L2, L3, L4, L5, L6 = sp.symbols('L1 L2 L3 L4 L5 L6')
    # 课后题5.2.b
    Btime = time.time()
    d1, d2, d3, d4, d5, d6, d7, d8 = 186.756, 184.549, 615.605, 126.951, 573.731, 116.549, 116.52, 102.156
    theta1, theta2, theta3, theta4, theta5, theta6 = np.pi / 2, np.pi / 2, np.pi / 2, np.pi / 2, np.pi / 2, np.pi / 2
    omega1 = [0, -1, 0]
    omega2 = [0, 0, -1]
    omega3 = [0, 0, -1]
    omega4 = [0, 0, -1]
    omega5 = [0, -1, 0]
    omega6 = [0, 0, 1]

    v1 = [-d8 + d6 - d4 + d2, 0, d5 + d3]
    v2 = [-d7, -d5 - d3, 0]
    v3 = [-d7, -d5, 0]
    v4 = [-d7, 0, 0]
    v5 = [-d8, 0, 0]
    v6 = [0, 0, 0]
    axis_list = [(omega1 + v1), (omega2 + v2), (omega3 + v3), (omega4 + v4), (omega5 + v5), (omega6 + v6)]

    theta_list = [theta1, theta2, theta3, theta4, theta5, theta6]  # 角度列表

    J = compute_jacobian(axis_list, theta_list, )
    Vd = [10, 10, 10, 0, 0, 0]
    theta_dot = np.linalg.inv(J) @ Vd
    # 删除多余的零并打印矩阵
    print(time.time() - Btime)
    print("关节速度：")
    print(theta_dot)
