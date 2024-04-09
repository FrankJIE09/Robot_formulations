import sympy as sp

# Define symbols
phi = sp.pi/2
R = sp.Matrix([[sp.cos(phi), -sp.sin(phi)],
               [sp.sin(phi), sp.cos(phi)]])
P = sp.Matrix([sp.Symbol('P_x'), sp.Symbol('P_y')])
P_dot = sp.Matrix([sp.Symbol('P_dot_x'), sp.Symbol('P_dot_y')])

# Calculate dot_R_transpose_P
dot_R_transpose_P = R.T * P_dot

# Print the result
print("dot_R_transpose_P:")
sp.pprint(dot_R_transpose_P)
