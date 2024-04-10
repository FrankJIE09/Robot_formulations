import numpy as np
from scipy.spatial.transform import Rotation

R1 = Rotation.from_euler('xyz', np.array([np.radians(0), np.radians(0), np.radians(180)]))
R2 = Rotation.from_euler('xyz', np.array([np.radians(0), np.radians(0), np.radians(-45)]))
T1 = np.eye(4)
T2 = np.eye(4)
T1[:3, :3] = R1.as_matrix()
T2[:3, :3] = R2.as_matrix()
T1[:3, 3] = np.array([1, 1, 0])
T2[:3, 3] = np.array([np.cos(np.radians(45)), np.sin(np.radians(45)), 0])
print(T1 @ T2)
print(Rotation.from_matrix((T1 @ T2)[:3, :3]).as_euler('xyz'))
Tsb = np.array([[np.cos(np.radians(30)), -np.sin(np.radians(30)), 0, 1],
                [np.sin(np.radians(30)), np.cos(np.radians(30)), 0, 2],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])
Tsc = np.array([[np.cos(np.radians(60)), -np.sin(np.radians(60)), 0, 2],
                [np.sin(np.radians(60)), np.cos(np.radians(60)), 0, 1],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])
T = Tsc @ np.linalg.inv(Tsb)
'''
print(T)

print(0.5 * (np.trace(T[:3, :3]) - 1))
theta = np.arccos(0.5 * (np.trace(T[:3, :3]) - 1))
print(theta)
'''
