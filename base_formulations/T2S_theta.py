import numpy as np

# 定义变换矩阵 T_sb 和 T_sc
T_sb = np.array([[np.cos(np.radians(30)), -np.sin(np.radians(30)), 0, 1],
                 [np.sin(np.radians(30)), np.cos(np.radians(30)), 0, 2],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]])

T_sc = np.array([[np.cos(np.radians(60)), -np.sin(np.radians(60)), 0, 2],
                 [np.sin(np.radians(60)), np.cos(np.radians(60)), 0, 1],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]])

# 计算 T_bc
T_bc =  T_sc@np.linalg.inv(T_sb)
p_bc = T_bc[:3, 3]

# 提取旋转部分 R_bc
R_bc = T_bc[:3, :3]

# 计算旋转角度 theta
theta = np.arccos((np.trace(R_bc) - 1) / 2)

# 计算旋转轴 omega
omega = (1 / (2 * np.sin(theta))) * np.array([R_bc[2, 1] - R_bc[1, 2],
                                              R_bc[0, 2] - R_bc[2, 0],
                                              R_bc[1, 0] - R_bc[0, 1]])
hat_omega = np.array([[0, -omega[2], omega[1]],
                      [omega[2], 0, -omega[0]],
                      [-omega[1], omega[0], 0]])
G_1 = 1 / theta*np.eye(3) - 1 / 2 * hat_omega + (1 / theta - 1 / 2 * (1 / np.tan(theta / 2))) * np.dot(hat_omega, hat_omega)
v = G_1 @ p_bc
# 输出结果
print("旋转角度 theta: {:.2f} 度".format(np.degrees(theta)))
print("旋转轴 omega: ", omega)
print("速度 v: ", v)
