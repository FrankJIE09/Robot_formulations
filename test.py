import sympy as sp

def logm(matrix):
    eigenvalues, eigenvectors = matrix.diagonalize()  # 对角化矩阵
    log_eigenvalues = sp.log(eigenvalues)  # 对特征值取对数
    log_matrix = eigenvectors @ sp.diag(*log_eigenvalues) @ eigenvectors.inv()  # 构造对数矩阵
    return log_matrix

# 示例用法
A = sp.Matrix([[2, 1], [1, 2]])
log_A = logm(A)
print("对数矩阵:")
print(log_A)
