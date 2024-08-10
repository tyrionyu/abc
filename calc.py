# 算术运算符
a = 10
b = 3
print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.3333333333333335
print(a % b)  # 1
print(a // b)  # 3
print(a ** b)  # 1000
print(a << 1)  # 20
print(a >> 1)  # 5

# 比较运算符
print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False

# 逻辑运算符
print(a > b and b > 0)  # True
print(a < b or b < 0)  # False
print(not (a > b))      # False

# 赋值运算符
a += 5
print(a)  # 15

# 位运算符
print(~a)  # -16
print(a & 15)  # 9
print(a | 5)  # 15

# 成员运算符
print(2 in [1, 2, 3])  # True
print(4 not in [1, 2, 3])  # True

# 身份运算符
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y)  # False，因为 x 和 y 是不同的对象
print(x is z)  # True，因为 z 引用了 x 的同一对象
