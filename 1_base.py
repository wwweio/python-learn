import keyword


list1 = ['Google', 'Runoob', 1997, 2000]
# for e in list1:
#     print(e)

# 1.注释 # ''' """
# for key in keyword.kwlist:
#     print(key)

# 2.行与缩进，python中使用缩进代表{}

# 3.多行语句
num1 = 1
num2 = 2
num3 = 3
# 换行时，使用反斜杠 \ 来代表仍是一行
total1 = num1 
+ num2 
+ num3

total2 = num1 \
+ num2 \
+ num3

print(total1)
print(total2)

# 3.引用标识符
text = r"这是一段带有转义符的文本\n"
print(text) 

# 4.打印不换行 末尾加end内容e
print("Hello", end=" ")
print("World")

# 5.删除引用 del 支持单个和多个引用（使用逗号隔开）的删除
x = 5
y = x
del x
print(y) 
print(x)  # 这里x的引用已经被删除，因此打印报错