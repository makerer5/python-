# python变量命名规则
# 1. 字母（Unicode字符），数字，下划线，不能使用特殊字符，不能数字开头（但可以下划线开头）
a = 123
b = 65
a1 = 12356
_a = 2356

# 2. 变量名是区分大小写的（大小写敏感，x和X是两个不同的变量名）
x = 2356
X = 'Python'

# 3. 不能使用Python中的关键字（Pyhton代码种有特殊含义的单词）和保留字（已经Python使用过的名字）
# if = 12365 这样Pythn就已经报错了
# print = 12356 
# print 函数在Python中代表输出的意思，我们虽然可以将变量命名为print,但在后续的代码中（使用print）会报错，无法使用print功能

# -------------------------------------------------------------------------------------------------------------------
# 4. 见名知意（变量名应简单明了）
age = 45
length = 23

# 5. 变量的命名使用全小写，多个单词用下划线进行连接（Snake case）
students_age = 18

# 如果想更改变量的名字，应鼠标左键双击变量名，选择Refactor--Rename，此时后续中所有涉及到该变量的代码会自动更正
print(a +b)


# input()函数
# input() 函数是Python 用来接受用户输入的函数，它允许程序暂停执行，等待用户输入一些文本，
# 然后将用户输入的内容作为“字符串”返回
name = input('what is your name? ')
print('Hi ' + name)

# 当你运行32-33行代码时，终端会提示你“what is your name?”
# 此时需要你在“？”后面输入你的名字，程序会继续执行，终端最后的输出内容为：Hi mosh
# print函数可以同时输出多个字符串的内容，每个字符串之间需要使用 “+” 连接

birth_year = input('Birth year: ')
age = 2019 - birth_year
print(age)
# 此时，你在终端看到报错信息：
'''Traceback (most recent call last):
  File "f:\project\pyhton学习笔记.py\day02.py", line 40, in <module>
    age = 2019 - birth_year
          ~~~~~^~~~~~~~~~~~
TypeError: unsupported operand type(s) for -: 'int' and 'str'' '''

# 从报错信息我们找到哪一个文件报错，并且是哪一行报错
# 报错原因是：input函数输出的内容为“str”，2019是一个“int”，我们不能用一个数字减去字符串
# 只需将 birth_year 类型转换为 int
# 在Python中用于转换的数据类型的函数还有：float()转换为小数，bool()转换为布尔值
# type 函数可以查询变量类型，和R中的 class，mode函数功能类似
birth_year = int(input('Birth year: '))
age = 2019 - birth_year
print(age)


# Python 中的引号
# Python 中单引号'',双引号""，三引号'''''
# 单引号：'"Python" for benningers'
# 双引号："'Python' for benningers"
# 三引号：''' Python for benninges '''
# 单引号和双引号只是为了区分着重引用，三引号内可以像word中一样，随意输出内容，此时这些内容都会被Python 识别为字符串
'''
Hi mosh
what is your name?
thank you 
'''


# 格式化字符串
# 当你需要在字符串中包含变量的值时，可以使用格式化字符串（f-string）
# 格式化字符串常用于需要动态地构建字符串的情况，尤其是当字符串中包含变量时。比如：打印输出，日志构建，数据库查询，Web应用查询
# 格式化字符串以字母"f"（可以是大写或小写）开头，后面跟着一个字符串，其中用花括号 {} 括起来的部分会被替换为变量的值。
'''
如果你需要输出 John [Smith] is a coder
使用字符串你可能会这么做
first = 'John'
last = 'Smith'
print(first + ' [' + last+ '] is a coder')
但这太过于麻烦
'''
first = 'John'
last = 'Smith'
msg = f'{first} + [{last}] + is a coder'
print(msg)



# if 语句
# Python 中if 语句用于判断条件是否为真，然后执行下面的程序
# 一个if 代表一个判断条件
# 如果要写一个：一个房子总价值100万美元，如果一个买家的信誉为优，则只需要支付10%的首付，如果为差，需要支付20%的首付
price = 1000000
has_good_credit = True
if has_good_credit:
    Down_payment = 0.1 * price
else:
    Down_payment = 0.2 * price
print(f'Down payment: ${Down_payment}')

price = 1000000
has_good_credit = False
has_bad_credit = False
if has_good_credit:
    Down_payment = 0.1 * price
elif has_bad_credit:
    Down_payment = 0.2 * price
else:
    Down_payment = 0.15 * price
print(f'Down payment: ${Down_payment}')





