import numpy as np

# 定义杆的长度
l = 1.0

# 定义关节角速度
omega = np.pi / 4

# 计算转换矩阵 T
T = np.array([[np.cos(omega * t), -np.sin(omega * t), 0, l * np.cos(omega * t)],
              [np.sin(omega * t), np.cos(omega * t), 0, l * np.sin(omega * t)],
              [0, 0, 1, 0],
              [0, 0, 0, 1]])

# 计算 T 的时间导数，即速度矩阵 V
d_T = np.array([[-np.sin(omega * t) * omega, -np.cos(omega * t) * omega, 0, -l * np.sin(omega * t) * omega],
                [np.cos(omega * t) * omega, -np.sin(omega * t) * omega, 0, l * np.cos(omega * t) * omega],
                [0, 0, 0, 0],
                [0, 0, 0, 0]])

print("速度矩阵 V:")
print(d_T)
