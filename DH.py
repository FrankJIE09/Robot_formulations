from roboticstoolbox import DHRobot, SE3
import numpy as np

# 定义 DH 参数
a = [0, 0.4318, 0.0203, 0, 0, 0]
d = [0.333, 0, 0, 0.316, 0, 0.0825]
alpha = [-np.pi/2, 0, np.pi/2, -np.pi/2, np.pi/2, 0]

# 定义关节角度
theta = [0, 0.7854, 0, 0.7854, 0, 0]

# 创建机器人模型
robot = DHRobot(
    [0, 1, 2, 3, 4, 5],
    a,
    d,
    alpha
)

# 计算末端到基坐标的转换矩阵
T = robot.fkine(theta)

# 打印转换矩阵
print("末端到基坐标的转换矩阵:")
print(T)
