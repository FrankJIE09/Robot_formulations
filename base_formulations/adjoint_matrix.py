import numpy as np
import sympy as sp
from POE.POE_dot import  *

def hat_map(vector):
    """
    Hat映射函数，将向量转换为斜对称矩阵
    """
    return np.array([[0, -vector[2], vector[1]],
                     [vector[2], 0, -vector[0]],
                     [-vector[1], vector[0], 0]])


def adjoint_transform(T):
    """
    计算SE(3)群的伴随变换矩阵
    """
    # 提取旋转矩阵R和平移向量p
    R = T[:3, :3]
    p = T[:3, 3]

    # 计算p的斜对称矩阵
    hat_p = hat_map(p)

    # 构建伴随变换矩阵Ad(T)
    upper_left = R
    upper_right = np.zeros((3, 3))
    lower_left = np.dot(hat_p, R)
    lower_right = R

    adjoint_matrix = np.block([[upper_left, upper_right],
                               [lower_left, lower_right]])

    return adjoint_matrix


if __name__ == '__main__':
    # 示例SE(3)转换矩阵T
    # 定义一个示例矩阵

    theta1,theta2 = sp.symbols('theta1 theta2')
    L1,L2 = sp.symbols('L1 L2')
    L = sp.symbols('L')
    omega1 = np.array([0, 0, 1])  # 旋转轴（单位向量）
    v1 = np.array([0, 0, 0])  # 线速度方向

    T1 = POE(omega1, v1, theta1)
    omega2 = np.array([0, 0, 1])  # 旋转轴（单位向量）
    v2 = np.array([0, -L1, 0])  # 线速度方向
    T2 = POE(omega2, v2, theta2)
    # 计算伴随变换矩阵Ad(T)
    Ad_T1 = adjoint_transform(T1)
    Ad_T2 = adjoint_transform(T1@T2)

    print(Ad_T2)
    Vb = np.array([0,0,  1, 0, -L1, 0])
    Vb2 =  np.array([0,0,  1, 0, -L1-L2, 0])
    print("伴随变换矩阵 Ad(T):")
    print(Ad_T1)
    print(sp.simplify(Ad_T2 @ Vb2))
