import sympy as sp

# 定义符号变量
theta1, theta2, theta3, theta4, theta5 = sp.symbols('theta1 theta2 theta3 theta4 theta5')
a1, a2, a3, a4, a5 = sp.symbols('a1 a2 a3 a4 a5')
d1, d2, d3, d4, d5 = sp.symbols('d1 d2 d3 d4 d5')
alpha0, alpha1, alpha2, alpha3, alpha4 = sp.symbols('alpha0 alpha1 alpha2 alpha3 alpha4')
k, s, phi = sp.symbols('k, s, phi ')

# 定义DH参数
DH_parameters = [
    {sp.Symbol('alpha'): -sp.pi / 2, sp.Symbol('a'): 0, sp.Symbol('d'): 0, sp.Symbol('theta'): phi},
    {sp.Symbol('alpha'): sp.pi / 2, sp.Symbol('a'): 0, sp.Symbol('d'): 0, sp.Symbol('theta'): k * s / 2},
    {sp.Symbol('alpha'): -sp.pi / 2, sp.Symbol('a'): 0, sp.Symbol('d'): (2 / k) * sp.sin(k * s / 2),
     sp.Symbol('theta'): 0},
    {sp.Symbol('alpha'): sp.pi / 2, sp.Symbol('a'): 0, sp.Symbol('d'): 0, sp.Symbol('theta'): k * s / 2},
    {sp.Symbol('alpha'): 0, sp.Symbol('a'): 0, sp.Symbol('d'): 0, sp.Symbol('theta'): -phi}
]


# 定义单位变换矩阵
def DH_transform(alpha, a, d, theta):
    return sp.Matrix([
        [sp.cos(theta), -sp.sin(theta) * sp.cos(alpha), sp.sin(theta) * sp.sin(alpha), a * sp.cos(theta)],
        [sp.sin(theta), sp.cos(theta) * sp.cos(alpha), -sp.cos(theta) * sp.sin(alpha), a * sp.sin(theta)],
        [0, sp.sin(alpha), sp.cos(alpha), d],
        [0, 0, 0, 1]
    ])


# 计算总的变换矩阵
T = sp.eye(4)
for params in DH_parameters:
    T = T * DH_transform(params[sp.Symbol('alpha')], params[sp.Symbol('a')], params[sp.Symbol('d')],
                         params[sp.Symbol('theta')])


T = sp.simplify(T)
T_inv = sp.simplify(T.inv())
T_diff_k = T.diff(k)
T_diff_phi = T.diff(phi)
T_diff_s = T.diff(s)

# 输出末端到基坐标的转换公式
print("末端到基坐标的转换公式:")
sp.pprint(T)
