import numpy as np
from scipy.spatial.transform import Rotation as R
from Jacobian.Jacobian_object import *
from scipy.linalg import logm, expm
from POE.POE_dot import *


def hat_to_SE3(v_b_hat):
    # 提取角速度和平移部分
    omega_hat = v_b_hat[:3, :3]
    v = v_b_hat[:3, 3]

    # 计算角速度向量
    omega = np.array([omega_hat[2, 1], omega_hat[0, 2], omega_hat[1, 0]])

    # 构造 SE(3) 中的元素

    return np.hstack((omega, v))


def inverse_kinematics2(theta1, theta2, l1, l2, Tsd, max_iter=100, tol=1e-6):
    for _ in range(max_iter):
        R1 = R.as_matrix(R.from_euler('xyz', np.array([0, 0, theta1]), degrees=True))
        R2 = R.as_matrix(R.from_euler('xyz', np.array([0, 0, theta2]), degrees=True))
        x = np.cos(np.deg2rad(theta1)) * l1 + np.cos(np.deg2rad(theta1 + theta2)) * l2
        y = np.sin(np.deg2rad(theta1)) * l1 + np.sin(np.deg2rad(theta1 + theta2)) * l2
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
        vb = hat_to_SE3(hat_vb.real)
        theta = np.array([[theta1, theta1],
                          [theta2, theta2]])

        theta_2 = np.rad2deg(theta + (np.linalg.pinv(Jb.astype(float)) @ np.vstack((vb, vb)).T))
        theta1, theta2 = theta_2[:, 0]
        print("theta1,theta2 =", theta_2[:, 0])
        # if


def inverse_kinematics(theta_list, axis_list, Tsd, max_iter=100, tol_w=1e-3, tol_v=1e-4):
    hat_v_Tsd = logm(Tsd)
    v_Tsd = hat_to_SE3(hat_v_Tsd.real)

    for _ in range(max_iter):
        T_prev = np.eye(4)
        for theta, axis, l in zip(theta_list, axis_list):
            T = POE(axis[:3], axis[3:], theta)
            T_prev = T_prev @ T
        M = np.eye(4)
        M[0, -1] = 2
        Tsb = np.array(M @ T_prev, dtype=float)
        # 计算机器人末端的姿态误差

        hat_vb = logm(np.linalg.inv(Tsb) @ Tsd)
        vb = hat_to_SE3(hat_vb.real)

        # 计算雅可比矩阵
        Jb = compute_jacobian(axis_list, theta_list)

        # 使用牛顿迭代法求解逆运动学
        delta_theta = (np.linalg.pinv(Jb.astype(float)) @ np.vstack((vb, vb)).T)[:, 0]
        theta_list += delta_theta
        print(np.rad2deg(theta_list))
        # 检查是否达到收敛条件
        hat_v_Tsb = logm(Tsb)
        v_Tsb = hat_to_SE3(hat_v_Tsb)

        if np.linalg.norm(v_Tsb[:3] - v_Tsd[:3]) < tol_w and np.linalg.norm(v_Tsb[3:] - v_Tsd[3:]) < tol_v:
            break

    return theta_list


if __name__ == '__main__':
    Tsd = np.array([[0, 1, 0, -0.5],
                    [0, 0, -1, 0.1],
                    [-1, 0, 0, 0.1],
                    [0, 0, 0, 1]])

    w1 = np.array([0, 0, 1])
    v1 = np.array([0, 0, 0])
    theta1 = 0.1
    H1 = 0.089
    W1 = 0.109
    W2 = 0.82
    L1 = 0.425
    L2 = 392
    H2 = 0.095
    w2 = np.array([0, 0, 1])
    v2 = np.array([-H1, 0, 0])
    theta2 = 0.1

    w3 = np.array([0, 1, 0])
    v3 = np.array([-H1, 0, L1])
    theta3 = 0.1

    w4 = np.array([0, 1, 0])
    v4 = np.array([-H1, 0, L1 + L2])
    theta4 = 0.1

    w5 = np.array([0, 0, -1])
    v5 = np.array([-W1, L1 + L2, 0])
    theta5 = 0.1

    w6 = np.array([0, 1, 0])
    v6 = np.array([H2 - H1, 0, L1 + L2])
    theta6 = 0.1
    axis_list = [np.concatenate((w1, v1)),
                 np.concatenate((w2, v2)),
                 np.concatenate((w3, v3)),
                 np.concatenate((w4, v4)),
                 np.concatenate((w5, v5)),
                 np.concatenate((w6, v6))
                 ]  # 轴向列表
    theta_list = [theta1, theta2, theta3, theta4, theta5, theta6]
    inverse_kinematics(theta_list, axis_list, Tsd, )
