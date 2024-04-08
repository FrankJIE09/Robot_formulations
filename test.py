import sympy as sp

# 定义符号变量
theta, phi = sp.symbols('theta phi')

# 定义表达式
expr = (-sp.sin(theta/2)**2*sp.cos(phi) + sp.cos(phi)*sp.cos(theta/2)**2)*sp.cos(phi) + sp.sin(phi)**2

# 将表达式中的 theta/2 合并为 theta
expr_simplified = sp.simplify(expr)
print("合并后的表达式：")
print(expr_simplified)
