import numpy as np

# 创建两个随机向量
A = np.random.rand(3)
B = np.random.rand(3)

# 计算 A × B 和 B × (-A)
cross_product_1 = np.cross(A, B)
cross_product_2 = np.cross(B, -A)

# 检查是否相等
if np.allclose(cross_product_1, cross_product_2):
    print("A × B 等于 B × (-A)")
else:
    print("A × B 不等于 B × (-A)")
