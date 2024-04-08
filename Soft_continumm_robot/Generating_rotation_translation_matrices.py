# Author: Frank & Chatgpt
# Edit Date: 2024-04-08
# Code Purpose: Functions for generating rotation and translation matrices in SE(3) space, and calculating affine transformation matrices
import numpy as np
import sympy as sp
def rot_SE3(axis, angle):
    """
    生成绕指定轴的旋转矩阵的SE(3)形式
    Args:
        axis: 旋转轴，'x'、'y' 或 'z'
        angle: 旋转角度，单位为弧度

    Returns:
        SE(3)形式的旋转矩阵
    """
    if axis == 'x':
        rotation_matrix = np.array([[1, 0, 0],
                                    [0, sp.cos(angle), -sp.sin(angle)],
                                    [0, sp.sin(angle), sp.cos(angle)]])
    elif axis == 'y':
        rotation_matrix = np.array([[sp.cos(angle), 0, sp.sin(angle)],
                                    [0, 1, 0],
                                    [-sp.sin(angle), 0, sp.cos(angle)]])
    elif axis == 'z':
        rotation_matrix = np.array([[sp.cos(angle), -sp.sin(angle), 0],
                                    [sp.sin(angle), sp.cos(angle), 0],
                                    [0, 0, 1]])
    else:
        raise ValueError("Axis must be 'x', 'y', or 'z'.")

    se3_matrix = sp.eye(4)
    se3_matrix[:3, :3] = rotation_matrix
    return se3_matrix


def trans(axis, distance):
    """
    生成沿指定轴平移的平移矩阵
    Args:
        axis: 平移轴，'x'、'y' 或 'z'
        distance: 平移距离

    Returns:
        平移矩阵
    """
    if axis == 'x':
        return np.array([[1, 0, 0, distance],
                         [0, 1, 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])
    elif axis == 'y':
        return np.array([[1, 0, 0, 0],
                         [0, 1, 0, distance],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])
    elif axis == 'z':
        return np.array([[1, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 1, distance],
                         [0, 0, 0, 1]])
    else:
        raise ValueError("Axis must be 'x', 'y', or 'z'.")


def calculate_affine_matrix(alpha, theta, R):
    """
    计算给定参数的仿射变换矩阵
    Args:
        alpha: alpha角度，单位为弧度
        theta: theta角度，单位为弧度
        R: R值

    Returns:
        仿射变换矩阵
    """
    rot_z_alpha = rot_SE3('z', -alpha)
    trans_z_Rsintheta = trans('z', R * sp.sin(theta))
    trans_x_R_1_minus_cos_theta = trans('x', R * (1 - sp.cos(theta)))
    rot_y_theta = rot_SE3('y', theta)
    rot_z_alpha_2 = rot_SE3('z', alpha)

    # 计算仿射变换矩阵
    affine_matrix = sp.Matrix(rot_z_alpha @ trans_z_Rsintheta @
                              trans_x_R_1_minus_cos_theta @ rot_y_theta @ rot_z_alpha_2)

    return affine_matrix


# 定义符号变量
alpha, theta, R = sp.symbols('alpha theta R')

# 计算仿射变换矩阵
affine_matrix = calculate_affine_matrix(alpha, theta, R)
# jac_alpha = affine_matrix.diff(alpha)
# jac_theta = affine_matrix.diff(theta)
# 打印带有符号变量的仿射变换矩阵
print("仿射变换矩阵:")
print(affine_matrix)
# print(jac_alpha)
# print(jac_theta)
# 提取仿射变换矩阵的旋转部分并转换为列表的列表
# 提取仿射变换矩阵的旋转部分
rotation_matrix_sympy = affine_matrix[:3, :3]

# 计算对数映射
S = sp.Matrix(sp.log(rotation_matrix_sympy))

# 提取轴角
theta = sp.sqrt(S[0, 1]**2 + S[1, 0]**2 + S[2, 0]**2)
axis = sp.Matrix([S[2, 1] - S[1, 2], S[0, 2] - S[2, 0], S[1, 0] - S[0, 1]]) / (2 * sp.sin(theta))

print("Rotation Axis:", axis)
print("Rotation Angle:", theta)