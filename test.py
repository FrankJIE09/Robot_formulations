import numpy as np

# Forward kinematics for 2R robot
def forward_kinematics(theta1, theta2, l1, l2):
    x = l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2)
    y = l1 * np.sin(theta1) + l2 * np.sin(theta1 + theta2)
    return x, y

# Jacobian matrix for 2R robot
def jacobian(theta1, theta2, l1, l2):
    J = np.zeros((2, 2))
    J[0, 0] = -l1 * np.sin(theta1) - l2 * np.sin(theta1 + theta2)
    J[0, 1] = -l2 * np.sin(theta1 + theta2)
    J[1, 0] = l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2)
    J[1, 1] = l2 * np.cos(theta1 + theta2)
    return J

# Inverse kinematics using Newton-Raphson iteration
def inverse_kinematics(x, y, l1, l2, theta_guess=np.array([0.0, 0.0]), max_iter=100, tol=1e-6):
    theta = theta_guess.copy()
    for _ in range(max_iter):
        x_fk, y_fk = forward_kinematics(theta[0], theta[1], l1, l2)
        error = np.array([x - x_fk, y - y_fk])
        if np.linalg.norm(error) < tol:
            break
        J = jacobian(theta[0], theta[1], l1, l2)
        delta_theta = np.linalg.lstsq(J, error, rcond=None)[0]
        theta += delta_theta
    return theta

# Example usage
if __name__ == "__main__":
    l1 = 1.0  # Length of link 1
    l2 = 1.0  # Length of link 2
    x_target = 1.5  # Target x position
    y_target = 1.0  # Target y position

    # Solve inverse kinematics
    theta_solution = inverse_kinematics(x_target, y_target, l1, l2)
    print("Inverse kinematics solution (theta1, theta2):", theta_solution)

    # Verify forward kinematics
    x_fk, y_fk = forward_kinematics(theta_solution[0], theta_solution[1], l1, l2)
    print("Forward kinematics result (x, y):", (x_fk, y_fk))
