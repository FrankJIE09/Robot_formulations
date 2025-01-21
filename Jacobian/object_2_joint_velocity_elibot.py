import numpy as np
import sympy as sp
from POE.POE_dot import POE
from base_formulations.adjoint_matrix import adjoint_transform
from base_formulations.rodrigures import *


def compute_jacobian(axis_list, theta_list):
    """
    根据给定的旋转轴列表和关节角列表计算机器人的雅可比矩阵。
    参数:
    axis_list : list - 包含每个关节的旋转轴向量和平移向量。
    theta_list : list - 包含每个关节的旋转角度。

    返回:
    jacobian : numpy.ndarray - 计算得到的雅可比矩阵。
    """
    assert len(axis_list) == len(theta_list), "轴数和角度数必须相同"
    axis_list = axis_list[::-1]
    theta_list = theta_list[::-1]
    J_list = []
    T_prev = np.eye(4)

    for axis, theta in zip(axis_list, theta_list):
        omega = np.array(axis)[:3]  # 提取旋转部分
        v = np.array(axis)[3:]  # 提取平移部分

        # 计算当前关节的变换矩阵
        T = POE(omega, v, -theta)

        # 计算伴随变换矩阵
        Ad_T = adjoint_transform(T_prev)

        # 构造扭矩向量
        S = np.hstack((omega, v))

        # 计算雅可比矩阵的当前列
        J = np.dot(Ad_T, S)
        J_list.append(sp.simplify(J))

        # 更新前一个变换矩阵
        T_prev = np.dot(T_prev, T)

    # 将雅可比矩阵反转并转换为浮点数格式
    return np.array(J_list[::-1]).T.astype(float)


def calculate_joint_velocity(Vd, theta):
    """theta_list = eval(theta_str)  # 将字符串转换为列表
    计算关节速度。
    参数:
    Vd : list - 速度向量。

    返回:
    theta_dot : numpy.ndarray - 计算得到的关节速度。
    """
    np.set_printoptions(precision=4, suppress=True)
    # 常量定义
    theta1, theta2, theta3, theta4, theta5, theta6 = theta
    d1, d2, d3, d4, d5, d6, d7, d8 = 186.756, 184.549, 615.605, 126.951, 573.731, 116.549, 116.52, 102.156
    omega1, omega2, omega3, omega4, omega5, omega6 = [0, 1, 0], [0, 0, -1], [0, 0, -1], [0, 0, -1], [0, -1, 0], [0, 0,
                                                                                                                  1]
    v1, v2, v3, v4, v5, v6 = [-d8 + d6 - d4 + d2, 0, d5 + d3], [-d7, -d5 - d3, 0], [-d7, -d5, 0], [-d7, 0, 0], [-d8, 0,
                                                                                                                0], [0,
                                                                                                                     0,
                                                                                                                     0]
    axis_list = [(omega1 + v1), (omega2 + v2), (omega3 + v3), (omega4 + v4), (omega5 + v5), (omega6 + v6)]
    theta_list = [theta1, theta2, theta3, theta4, theta5, theta6]  # 角度列表

    # 计算雅可比矩阵
    J = compute_jacobian(axis_list, theta_list)

    # 计算关节速度
    theta_dot = np.linalg.inv(J) @ Vd
    return theta_dot


if __name__ == '__main__':
    # 示例调用
    Vd = [10, 10, 10, 0, 0, 0]
    theta1, theta2, theta3, theta4, theta5, theta6 = np.pi / 2, np.pi / 2, np.pi / 2, np.pi / 2, np.pi / 2, np.pi / 2

    theta_dot = calculate_joint_velocity(Vd, [theta1, theta2, theta3, theta4, theta5, theta6])
    print("关节速度：")
    print(theta_dot)
