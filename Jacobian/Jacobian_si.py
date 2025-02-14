import numpy as np
import sympy as sp
from POE.POE_dot import *
from base_formulations.adjoint_matrix import *
from base_formulations.rodrigures import *


def compute_jacobian(axis_list, theta_list, ):
    # assert len(axis_list) == len(theta_list) "轴数、角度数和长度数必须相同"

    J_list = []
    T_prev = np.eye(4)

    for axis, theta in zip(axis_list, theta_list):
        omega = np.array(axis)[0:3]
        v = np.array(axis)[3:]

        # 计算当前变换矩阵
        T = POE(omega, v, theta)

        # 计算伴随变换矩阵Ad(T)
        Ad_T = adjoint_transform(T_prev)

        # 构造齐次变换矩阵的对数映射矩阵
        S = np.hstack((omega, v))

        # 计算雅可比矩阵
        J = np.dot(Ad_T, S)
        J_list.append(sp.simplify(J))

        # 更新T_prev
        T_prev = np.dot(T_prev, T)

    return np.array(J_list).T


if __name__ == '__main__':
    np.set_printoptions(precision=3,suppress=True)

    # 示例调用
    theta1, theta2, theta3, theta4, theta5, theta6 = sp.symbols('theta1 theta2 theta3 theta4 theta5 theta6')
    L1 = 100
    theta1, theta2, theta3, theta4 =0,0,0,0
    axis_list = [[0, 0, 1, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, -L1], ]

    theta_list = [theta1, theta2, theta3, theta4]  # 角度列表

    J = compute_jacobian(axis_list, theta_list, )
    print(J)
    print(J.T)
    exit()
    # 例题5.2
    axis_list = [[0, 0, 1, 0, 0, 0],
                 [0, 0, 1, 0, -L1, 0],
                 [0, 0, 1, 0, -L1 - L2, 0],
                 [0, 0, 0, 0, 0, 1]]  # 轴向列表
    theta_list = [theta1, theta2, theta3, theta4]  # 角度列表

    J = compute_jacobian(axis_list, theta_list, )
    # 删除多余的零并打印矩阵
    print("空间雅可比的转置为：")
    print(J.T)
    print("物体雅可比：")
