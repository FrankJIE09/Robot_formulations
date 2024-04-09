import numpy as np


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


# 示例SE(3)转换矩阵T
# 定义一个示例矩阵
T = np.array([[-1, 0, 0, 4],
              [0, 1, 0, 0.4],
              [0, 0, -1, 0],
              [0, 0, 0, 1]])

# 计算伴随变换矩阵Ad(T)
Ad_T = adjoint_transform(T)
Vb = np.array([0, 0, -2, 2.8, 4, 0])

print("伴随变换矩阵 Ad(T):")
print(Ad_T)
print(Ad_T@Vb)



