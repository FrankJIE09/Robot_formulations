import sympy as sp

# 定义符号变量
phi, theta, s = sp.symbols('phi theta s')

# 定义DH参数



# 定义单位变换矩阵



# 计算总的变换矩阵
T = sp.eye(4)
for params in DH_parameters:
    T = T * DH_transform(params[sp.Symbol('alpha')], params[sp.Symbol('a')], params[sp.Symbol('d')],
                         params[sp.Symbol('theta')])

# 输出末端到基坐标的转换公式

T_inv = T.inv()
T_diff_theta = T.diff(theta)
T_diff_phi = T.diff(phi)
print("末端到基坐标的转换公式:")
sp.pprint(T)
