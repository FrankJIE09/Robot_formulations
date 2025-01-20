from Jacobian_si import *

theta1, theta2, theta3, theta4, theta5, theta6 = sp.symbols('theta1 theta2 theta3 theta4 theta5 theta6')
L1, L2, L3, L4, L5, L6 = sp.symbols('L1 L2 L3 L4 L5 L6')
L = sp.symbols('L')

# 课后题5.2.b
axis_list = [[0, 0, 1, 0, 0, 0],
             [0, 0, 1, 0, -L1, 0],
             [0, 0, 1,0,  -L1-L2, 0],
             [0, 0, 0, 0, 0, 1],

             ]  # 轴向列表
theta_list = [theta1, theta2, theta3, theta4]  # 角度列表

J = compute_jacobian(axis_list, theta_list, )
# 删除多余的零并打印矩阵
print("空间雅可比的转置为：")
for row in J: 
    for elem in row:
        if elem.is_Float:
            print("{:.1f}".format(elem), end=', ')
        else:
            print(elem, end=', ')
    print()  # 换行

