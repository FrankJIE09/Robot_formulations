import numpy as np

# 定义矩阵
A = np.array([[1, 0, 0, 0],
              [-1,0, 0, 0],
              [0, 10, 1, 0],
              [0, 0, 0, 1]])

# 计算特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(A)

# 对特征值取对数
log_eigenvalues = np.log(eigenvalues)

# 构造对数矩阵
log_A = eigenvectors @ np.diag(log_eigenvalues) @ np.linalg.inv(eigenvectors)

print("矩阵的对数:")
print(log_A)
