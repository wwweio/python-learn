# 1.赋值运算符:海象运算符 一般只能用在表达式中，赋值并返回赋值
# if(a := 10 * 9) > 10 :
#     print(a)

# 幂赋值运算
# print(10 ** 2)



# 2.位运算
a = 60
b = 13

# print(bin(a)[2:])
# print(format(b, '08b'))
# print(a&b)
# print(a|b)
# print(a^b)
# # 左移就是  乘2的倍数
# print(a << 2)
# # 右移就是  除2的倍数
# print(a >> 2)


# 3.逻辑运算符 
# # 两个整数 and 取大数值
# print(a and b)
# # 两个整数 and 取小数值
# print(a or b)
# # not代表取反的意思
# print(not a)

print(30 and 40)
print(30 or 40)
print(not 30)
print(not (30 and 40))
print(not (30 or 40))

# 在py中，非0整数为True 0为False
# print(bool(30))
# print(bool(-30))
# print(bool(0))
# print(bool(-0))

# 逻辑运算符中
# 有and运算有True，则为True
# print(True and False)
# print(True or False)
# print(True and True)
# print(True or True)
# print(False and False)
# print(False or False)