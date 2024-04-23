import numpy as np
from scipy.spatial.transform import Rotation as R
from Jacobian.Jacobian_object import *
from scipy.linalg import logm
def hat_to_SE3(v_b_hat):
    # 提取角速度和平移部分
    omega_hat = v_b_hat[:3, :3]
    v = v_b_hat[:3, 3]

    # 计算角速度向量
    omega = np.array([omega_hat[2, 1], omega_hat[0, 2], omega_hat[1, 0]])

    # 构造 SE(3) 中的元素

    return np.hstack((omega,v))
# def inverse_kinematics(x, y, l1, l2, theta_guess=np.array([0.0, 0.0]), max_iter=100, tol=1e-6):
#     theta = theta_guess.copy()
#     for _ in range(max_iter):
#         x_fk, y_fk = forward_kinematics(theta[0], theta[1], l1, l2)
#         error = np.array([x - x_fk, y - y_fk])
#         if np.linalg.norm(error) < tol:
#             break
#         J = jacobian(theta[0], theta[1], l1, l2)
#         delta_theta = np.linalg.lstsq(J, error, rcond=None)[0]
#         theta += delta_theta
#     return theta
if __name__ == '__main__':
    R1 = R.as_matrix(R.from_euler('xyz', np.array([0, 0, 0]), degrees=True))
    R2 = R.as_matrix(R.from_euler('xyz', np.array([0, 0, 30]), degrees=True))
    x = np.cos(np.deg2rad(0)) * 1 + np.cos(np.deg2rad(30)) * 1
    y = np.sin(np.deg2rad(0)) * 1 + np.sin(np.deg2rad(30)) * 1
    Tsb = np.eye(4)
    Tsb[:3, :3] = R1 @ R2
    Tsb[:3, -1] = np.array([x, y, 0])
    print(Tsb)
    R1 = R.as_matrix(R.from_euler('xyz', np.array([0, 0, 30]), degrees=True))
    R2 = R.as_matrix(R.from_euler('xyz', np.array([0, 0, 90]), degrees=True))
    x = np.cos(np.deg2rad(30)) * 1 + np.cos(np.deg2rad(30 + 90)) * 1
    y = np.sin(np.deg2rad(30)) * 1 + np.sin(np.deg2rad(30 + 90)) * 1

    Tsd = np.eye(4)
    Tsd[:3, :3] = R1 @ R2
    Tsd[:3, -1] = np.array([x, y, 0])
    print(Tsd)
    w1 = np.array([0, 0, 1])
    v1 = np.array([0, 2, 0])
    theta1 = 0
    w2 = np.array([0, 0, 1])
    v2 = np.array([0, 1, 0])
    theta2 = np.deg2rad(30)
    axis_list = [np.concatenate((w1, v1)),
                 np.concatenate((w2, v2))]  # 轴向列表
    theta_list = [theta1, theta2, ]  # 角度列表
    Jb = compute_jacobian(axis_list, theta_list, )
    print(Jb)
    hat_vb = logm(np.linalg.inv(Tsb) @ Tsd)
    vb = hat_to_SE3(hat_vb)
    theta = np.array([theta1, theta2])
    theta2 = np.rad2deg(theta.T + (np.linalg.pinv(Jb.astype(float)) @ np.vstack((vb,vb)).T)[:,0])
