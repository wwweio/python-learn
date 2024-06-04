import random 
# 数字
# 1）特殊的数组，布尔值
# boolean 
# 判断类型的两种方法，type 和 isinstance
# 区别：type 是判断变量类型，isinstance 是判断变量是否属于某个类型
# 在python中bool可以认为是int的子类，可以和数字相加。True = 1, False = 0
a = 1
flag = True
# print(type(flag) == int)
# print(isinstance(flag, int))

# 2）类型 整数、浮点数、复数
# 整数 1.无大小限制（可以当做Java中的long来使用）2.整数可以用十六进制和八进制来表示
# print(0xff)
# print(0o37)
# 浮点数可以用科学计数法表示 （2e2 即 2的平方 = 4）
# print(2e2)
# print(32.3e+18)
# print(type(10_00) == int)

# 3）转换 直接使用对应类型的关键字即可转换
#转换为整数
# print(int(10.23))
# print(float('10'))
# complex_num = complex(10)
# print(type(complex_num))
# print(complex_num)

# 4）运算
# 不同类型的数混合运算时会将整数转换为浮点数

# 除法求整数。注意：得到的并不一定是整数类型的数，如果分子、分母有小数，则结果为小数
# 除法求浮点数。注意：得到的结果一定是浮点类型的数
a = 10//3
# 除法求浮点数
b = 10/3
# 乘方
c = 10**3
print(a, b, c)
# 注意：在交互模式中，'_'作为 存储上一个表达式的结果 的变量

# 5）函数 
# 1.choice函数 随机选择一个元素 random.choice随机选择列表/元组/字符串的随机项
# print(random.choice(range(10)))
# sample函数 从列表/元组/字符串中随机选择n个元素， 注意：不会修改原内容
list = random.sample('31345adgdfg', 5)
# print(list)
# join函数 将列表/元组/字符串中的元素连接成字符串
# print(''.join(list))

# 2.round函数 四舍五入函数 奇进偶弃
# 偶数：<=0.5 舍去  > 0.5 进1
# 奇数：< 0.5 舍去  >= 0.5 进1
print(round(10.5))
print(round(11.5))


