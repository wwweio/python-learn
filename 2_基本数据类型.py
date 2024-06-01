# 字符串转换为int值时.需要先转换为float才能再转换为int
a = '123.456'
print(type(a))
print(int(float(a)))

# python 变量就是变量，没有类型，类型是指变量在内存中的对象类型

# 1.变量赋值 python可以同时为多个对象赋值
# 1）同时为多个对象赋值
a = b = c = 1
print(a, b, c)
# 2）同时为多个变量赋不同的值
a, b, c = 1, 2, "haha"
print(a, b, c)

# 2.变量类型
# 3个不可变类型：Number（bool可以认为是int的子类） String Tuple(元组)
# 3个可变类型： List Dict Set



