import numpy as np


def rodrigues_formula(v, theta):
    """
    计算 Rodrigues' formula
    Args:
        v: 旋转轴的单位向量，形如 [vx, vy, vz]
        theta: 旋转角度，单位为弧度

    Returns:
        旋转矩阵
    """
    # 将旋转轴单位化
    v_normalized = v / np.linalg.norm(v)

    # 计算反对称矩阵
    hat_v = np.array([[0, -v_normalized[2], v_normalized[1]],
                      [v_normalized[2], 0, -v_normalized[0]],
                      [-v_normalized[1], v_normalized[0], 0]])

    # 计算旋转矩阵
    R = np.eye(3) + np.sin(theta) * hat_v + (1 - np.cos(theta)) * np.dot(hat_v, hat_v)

    return R

if __name__ == '__main__':

    # 定义旋转轴和旋转角度
    v = np.array([1, 0, 0])  # x轴
    theta = np.pi / 2  # 绕x轴旋转90度

    # 计算旋转矩阵
    R = rodrigues_formula(v, theta)
    R1 = rodrigues_formula(np.array([0, 1, 0]), -np.pi / 2)
    R2 = rodrigues_formula(np.array([1, 0, 0]), np.pi / 2)
    R3 = rodrigues_formula(np.array([1, 0, 0]), -np.pi / 2)
    R4 = rodrigues_formula(np.array([1 / np.sqrt(5), 2 / np.sqrt(5), 0]), np.sqrt(5))
    Rx = rodrigues_formula(np.array([1, 0, 0]), np.radians(30))
    Ry = rodrigues_formula(np.array([0, 1, 0]), np.radians(180))
    Rz = rodrigues_formula(np.array([0, 0, 1]), np.radians(180))
    multi_solution = rodrigues_formula(np.array([1 / np.sqrt(2), 0, 1 / np.sqrt(2)]), np.radians(180))
    print(Rz @ Ry)
    '''
    
    Rs_b = Rx @ Ry @ Rz
    Rb_s = Rs_b.T
    ps = np.array([1, 2, 3])
    pb = Rb_s @ ps
    print("pb:\n", pb)
    print("Rsa: \n", R1 @ R2)
    print("Rsb: \n", R3)
    print("R4: \n", R4)
    
    print("旋转矩阵：")
    print(R)
    '''
