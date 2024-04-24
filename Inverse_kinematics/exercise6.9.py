import numpy as np
from scipy.spatial.transform import Rotation as R
from Jacobian.Jacobian_object import *
from scipy.linalg import logm,expm


def hat_to_SE3(v_b_hat):
    # 提取角速度和平移部分
    omega_hat = v_b_hat[:3, :3]
    v = v_b_hat[:3, 3]

    # 计算角速度向量
    omega = np.array([omega_hat[2, 1], omega_hat[0, 2], omega_hat[1, 0]])

    # 构造 SE(3) 中的元素

    return np.hstack((omega, v))

def inverse_kinematics(theta1, theta2, l1, l2, Tsd, max_iter=100, tol=1e-6):
    for _ in range(max_iter):
        R1 = R.as_matrix(R.from_euler('xyz', np.array([0, 0, theta1]), degrees=True))
        R2 = R.as_matrix(R.from_euler('xyz', np.array([0, 0, theta2]), degrees=True))
        x = np.cos(np.deg2rad(theta1)) * l1 + np.cos(np.deg2rad(theta1+theta2)) * l2
        y = np.sin(np.deg2rad(theta1)) * l1 + np.sin(np.deg2rad(theta1+theta2)) * l2
        print("x,y = ", x, y)
        Tsb = np.eye(4)
        Tsb[:3, :3] = R1 @ R2
        Tsb[:3, -1] = np.array([x, y, 0])
        # print(Tsb)
        w1 = np.array([0, 0, 1])
        v1 = np.array([0, 2, 0])
        theta1 = np.deg2rad(theta1)
        w2 = np.array([0, 0, 1])
        v2 = np.array([0, 1, 0])
        theta2 = np.deg2rad(theta2)
        axis_list = [np.concatenate((w1, v1)),
                     np.concatenate((w2, v2))]  # 轴向列表
        theta_list = [theta1, theta2, ]  # 角度列表
        Jb = compute_jacobian(axis_list, theta_list, )
        # print(Jb)
        hat_vb = logm(np.linalg.inv(Tsb) @ Tsd)
        print(Tsb)
        vb = hat_to_SE3(hat_vb.real)
        theta = np.array([[theta1, theta1],
                          [theta2, theta2]])

        theta_2 = np.rad2deg(theta + (np.linalg.pinv(Jb.astype(float)) @ np.vstack((vb, vb)).T))
        theta1, theta2 = theta_2[:, 0]
        print("theta1,theta2 =", theta_2[:, 0])
        # if


if __name__ == '__main__':
    thetad_1 = 90
    thetad_2 = 120
    R1 = R.as_matrix(R.from_euler('xyz', np.array([0, 0, thetad_1]), degrees=True))
    R2 = R.as_matrix(R.from_euler('xyz', np.array([0, 0, thetad_2]), degrees=True))
    x = np.cos(np.deg2rad(thetad_1)) * 1 + np.cos(np.deg2rad(thetad_1 + thetad_2)) * 1
    y = np.sin(np.deg2rad(thetad_1)) * 1 + np.sin(np.deg2rad(thetad_1 + thetad_2)) * 1

    Tsd = np.eye(4)
    Tsd[:3, :3] = R1 @ R2
    Tsd[:3, -1] = np.array([x, y, 0])
    print(Tsd)
    inverse_kinematics(0, 30, 1, 1, Tsd, 10)
