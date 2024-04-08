import numpy as np

def hat_map_so3(v):
    """
    将三维向量 v 映射到 so(3) 的 hat 映射结果
    """
    return np.array([[0, -v[2], v[1]],
                     [v[2], 0, -v[0]],
                     [-v[1], v[0], 0]])
def hat_map_se3(xi):
    """
    将六维向量 xi 映射到 se(3) 的 hat 映射结果
    """
    v = xi[:3]
    w = xi[3:]
    return np.block([
        [hat_map_so3(w), v[:, np.newaxis]],
        [np.zeros(3), 0]
    ])
# 示例向量
v = np.array([1, 2, 3])

# 计算 hat 映射结果
hat_v = hat_map_so3(v)
print("hat 映射结果:")
print(hat_v)


# 示例向量
xi = np.array([1, 2, 3, 0.1, 0.2, 0.3])

# 计算 hat 映射结果
hat_xi = hat_map_se3(xi)
print("hat 映射结果:")
print(hat_xi)
