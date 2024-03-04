# Python 逻辑运算符  'and' 'or' 'not'
# and
'''and 运算符用于连接两个条件，如果两个条件都为真（True），
那么整个表达式的结果为真（True）。否则，只要有一个条件为假（False），
整个表达式的结果就为假（False）。
'''
has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print('Eligible for loan')

'''
or 运算符用于连接两个条件，如果两个条件中至少有一个为真（True），
整个表达式的结果就为真（True）。只有当两个条件都为假（False）时，
整个表达式的结果才为假（False）。
'''
if has_high_income or has_good_credit:
    print('Eligible for loan')

'''
not 运算符用于对条件取反。如果条件为真（True），
not 将返回假（False）；如果条件为假（False），not 将返回真（True）。
在 Python 中，你不能直接在条件语句中使用 not 作为连接运算符，
而是必须使用逻辑运算符（如 and 或 or）将其与其他条件语句连接起来。
'''
# 如果一个人信誉良好且没有犯罪记录，那么他可以获得贷款
has_good_criminal = False
has_good_credit = True
if has_good_credit and not has_good_criminal:
    print('Eligible for loan')



# while 循环
# 当你需要重复执行某些代码块直到某个条件不再满足时，就可以使用 Python 中的 while 循环。
# while 循环的语法结构如下：
'''
while condition:
    # 在条件为真时执行的代码块
'''

# 下面是一个模拟汽车控制台的程序，当用户输入‘start’启动汽车，‘stop’停止汽车，‘help’获得帮助文件
# 当用户输入两次“start”时，程序会提示“Car already to the started”
# 用户输入两次“stop”时，程序提示“Car already to the stopped”
command = ""
started = False
while command != 'quit':
    command = input('> ').lower()
    if command == 'start':
        if started:
            print("Car already to the started")
        else:
            started = True
            print('Car started ... Ready to go!')
    elif command == 'stop':
        if not started:
            print("Car already to the stopped")
        else:
            started = False
            print('Car is stopped')
    elif command == 'help':
        help = '''
        start - to the car
        stop - to the stop
        quit - to quit
        '''
        print(help)
    elif command == 'quit':
        break
    else:
        print("I don't understand that")

# 一个简单的登录系统，用户必须输入正确的用户名和密码才能登录。如果用户输入错误，他们将有几次重试的机会。
correct_users = 'admin'
correct_password = '123456'
password_number = 0
password_limit = 3
while password_number < password_limit:
    users = input('Users name: ')
    if users == correct_users:
        password = input('Password: ')
        if password == correct_password:
            print("Wellcome!")
            break
        else:
            print('Failed!')
            password_number += 1
    else:
        print("Users name failed")
        password_number += 1


# for 循环
# for 循环是一种用于遍历可迭代对象（iterable）中元素的控制流结构。
# 在 Python 中，可迭代对象包括列表（list）、元组（tuple）、集合（set）、字典（dictionary）等，以及字符串等序列类型。
# for 循环的基本语法如下：
'''
for item in iterable:
    # 在每次迭代中执行的代码块
'''
# 在每次循环迭代中，变量 item 将依次取可迭代对象 iterable 中的元素，直到所有元素都被遍历完毕为止。
# 在循环体中，你可以对每个元素进行操作，或根据需要执行其他操作。
prices = [10,20,30]
total = 0
for item in prices:
   total += item
print(total)


# 嵌套循环
# 在一个循环内部包含另一个循环。这种结构允许你在每次外部循环迭代时执行内部循环。
x = 4
y = 3
for x in range(x):
    for y in range(y):
        print(f'({x},{y})')

numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += '*'
    print(output)

# 打印一个乘法表
for x in range(1,11):
    for y in range(1,11):
        print(x * y, end='\t')
    print()

# 找出列表中最大的数
numbers = [2,5,6,1,45,65,1,2]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# 删除列表中重复的元素
# 在这个问题中，我们可以挑选出不重复的元素，然后赋值给新的列表
numbers = [2,5,6,1,45,65,1,2]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)