import time
# 字符串
# name = 'jack'
# print(name)
# name = 'ma'
# print(name)

# name = 'jack'
# print(name[-2])

# input("\n\n按下 enter 键后退出。")

# 注意python中的字符串是不可变的，合并之后的字符串属于是新的字符串
# 1.引用标识符 单引号、双引号都可以

# 2.字符串访问
var = "www.nobi.com"
print(len(var))
# #1）通过下标访问  python分为前后下标
# print(var[0])
# print(var[-1])

# #2）标识符 : 可以代表起始和终止位置的下标，遵循左闭右开原则
# # 全部字符
# print(var[:])
# # :在前，表示从0开始，展示n个字符（也就是n-1的下标处结束）
# print(var[:5])
# # :在后，表示从下标处开始到末尾结束
# print(var[5:])

# # 3.字符串的更新 
# print(var[4:] + "/python.html")


# 4.转义符
# \n换行
# print('asg \\n sadrghsdrg ')

# 示例：使用\r打印百分比
# \r回车
# range函数前开后闭，不包括括号内的数字
# for a in range(100):
#     # {:2}格式化字符串占位，后面的内容保持长度为3为的空间，不足时使用空格填充
#     print('\r{:2}%'.format(a), end=' ')
#     time.sleep(0.05)

# # 铃声
# print('\a')

# for i in range(101):
#     print("\r{:3}%".format(i),end=' ')
#     time.sleep(0.05)



# 5.运算符
# 1）重复输出字符串 *
# web = 'memos.com'
# print(web*3)

# # 2)判断是否包含某种字符
# print('com' in web)
# print('wweio' not in web)

# # 3)原始字符串打印 字符串前使用r就可以。（不区分大小写）
# print('asg \\n sadrghsdrg ')
# print(r'asg \\n sadrghsdrg ')
# print(R'asg \\n sadrghsdrg ')


# 6.格式化
# 使用%来格式化 不推荐，用起来太繁琐了
# print('my name is %s. I am %f' % ('jack', 18.8))

# # 使用占位符
# print('my name is {}. I am {}'.format('jack', '18'))
# print('my name is {name}. I am {age}'.format(name = 'jack', age = '18'))

# 通过字典设置参数  **代表解包，然后传递给format函数作为关键字参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
 
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的 

# 通过对象方式设置
class User(object):
    def __init__(self, value):
        self.value = value 
value = User(1)
print('value的值为{0.value}'.format(value))

# 数字格式化
# 7.三引号 大赞，脱离转义符泥潭
long_str = '''这是一段非常长的长文本。\r真的真的 
你要你\t猜猜\n 啊哈哈哈
'''
print(long_str)

# 8.f-string
name = 'jack'
print(f'hello {name}')

w = {'name': 'ww', 'url': 'www.admin.com'}
print(f'{w["name"]}: {w["url"]}')

# 3.8版本可以使用=展示整个表达式
print(f'{1+1}')  # 3.6开始支持
print(f'{1+1=}') # 3.8开始支持


# 9.字符串内建函数  
print(name.title())
# python中带有方法带有双括号时，会调用方法，不带括号只是打印对于方法本身的引用信息
# <built-in method swapcase of str object at 0x0000018CD4644570>
# print(name.swapcase)
print(name.swapcase())