import numpy as np
from scipy.linalg import logm
import sympy as sp


# 定义矩阵

def log_matrix(A):
    # 计算特征值和特征向量
    eigenvalues, eigenvectors = np.linalg.eig(A)

    # 对特征值取对数
    log_eigenvalues = np.log(eigenvalues)

    # 构造对数矩阵
    log_A = (eigenvectors @ np.diag(log_eigenvalues) @ np.linalg.inv(eigenvectors)).real
    return log_A
    # print("矩阵的对数:")
    # print(log_A)


def log_m(matrix):
    eigenvalues, eigenvectors = matrix.diagonalize()  # 对角化矩阵
    log_eigenvalues = sp.log(eigenvalues)  # 对特征值取对数
    log_matrix = eigenvectors @ sp.diag(log_eigenvalues)[0] @ eigenvectors.inv()  # 构造对数矩阵
    return log_matrix


# if __name__ == '__main__':
#     A = sp.Matrix([[6.29482353e-17, -1.00000000e+00, 0.00000000e+00,
#                    -8.66025404e-01],
#                   [1.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#                    1.50000000e+00],
#                   [0.00000000e+00, 0.00000000e+00, 1.00000000e+00,
#                    0.00000000e+00],
#                   [0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#                    1.00000000e+00]])
#     logm(A)
