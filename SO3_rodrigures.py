import numpy as np
from scipy.spatial.transform import Rotation as R

def rotation_matrix_to_axis_angle(R):
    # 计算旋转轴的方向
    theta = np.arccos((np.trace(R) - 1) / 2)
    if np.isclose(theta, 0):
        # 当旋转角度接近于0时，旋转轴可以是任意方向，这里选择一个任意的非零向量作为旋转轴
        v = np.array([1, 0, 0])
    else:
        v = (1 / (2 * np.sin(theta))) * np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]])
    return v, theta


# 定义一个随机的旋转矩阵
R_matrix = np.array([[0, -1, 0], [0, 0, -1], [1, 0, 0]])
rotation = R.from_matrix(R_matrix)
rotvec2 = rotation.as_rotvec()
print(rotvec2)
# 计算旋转矢量和角度
rotvec, angle = rotation_matrix_to_axis_angle(R_matrix)

print("旋转矩阵 R:")
print(R_matrix)
print("旋转矢量 rotvec:")
print(rotvec)
print("旋转角度 theta:")
print(np.degrees(angle))  # 将弧度转换为角度进行显示
