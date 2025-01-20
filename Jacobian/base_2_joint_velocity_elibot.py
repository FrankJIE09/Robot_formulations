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

    return np.array(J_list)


def calculate_joint_velocity(Vd, theta1, theta2, theta3, theta4, theta5, theta6):
    """
    计算关节速度。
    参数:
    Vd : list - 速度向量。

    返回:
    theta_dot : numpy.ndarray - 计算得到的关节速度。
    """
    np.set_printoptions(precision=4, suppress=True)
    # 常量定义
    d1, d2, d3, d4, d5, d6, d7, d8 = 186.756, 184.549, 615.605, 126.951, 573.731, 116.549, 116.52, 102.156
    omega1, omega2, omega3, omega4, omega5, omega6 = [0, 0, -1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 0, -1], [0, -1,
                                                                                                               0]
    v1, v2, v3, v4, v5, v6 = [0, 0, 0], [-d1, 0, 0], [-d1, 0, d3], [-d1, 0, d3 + d5], [-d2 + d4 - d6, d3 + d5, 0], [
        d1 - d7, 0, -d3 - d5]
    axis_list = [(omega1 + v1), (omega2 + v2), (omega3 + v3), (omega4 + v4), (omega5 + v5), (omega6 + v6)]
    theta_list = [theta1, theta2, theta3, theta4, theta5, theta6]  # 角度列表

    # 计算雅可比矩阵
    J = compute_jacobian(axis_list, theta_list)

    # 计算关节速度
    J = np.array(J, dtype=np.float64)  # Convert J to a numeric array if it's not
    Vd = np.array(Vd, dtype=np.float64)  # Ensure Vd is also a numeric array

    theta_dot = np.linalg.inv(J) @ Vd
    return theta_dot


if __name__ == '__main__':
    # 示例调用
    Vd = [10, 10, 10, 0, 0, 0]
    theta1, theta2, theta3, theta4, theta5, theta6 = np.pi / 2, np.pi / 2, np.pi / 2, np.pi / 2, np.pi / 2, np.pi / 2

    theta_dot = calculate_joint_velocity(Vd, theta1, theta2, theta3, theta4, theta5, theta6)
    print("关节速度：")
    print(theta_dot)
