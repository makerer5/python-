# tuple 元组
# 在 Python 中，元组（tuple）是一种有序、不可变的数据类型，类似于列表，但元组中的元素不能被修改。
# 元组使用圆括号 () 来表示，其中的元素可以是任意类型，并且可以包含重复的元素。
# 在元组中，你可以存储多种类型的数据，包括整数、浮点数、字符串等。

tuple = (1,2,3,4,5)

# 元组与列表的主要区别在于：
'''
1. 不可变性（Immutable）：元组一旦创建后，其元素就不能被修改、添加或删除。这意味着你不能向元组中添加新元素，也不能修改现有元素的值。
2. 使用圆括号：元组使用圆括号 () 来表示，而列表使用方括号 []。
'''

# unpacking 解包
# 在 Python 中，解包（unpacking）是指将序列（如列表、元组、集合等）中的元素解包并赋值给多个变量的过程。
# 这种功能使得我们可以方便地从序列中提取并使用其中的元素。
# 解包针对有序数据类型，如列表，字符串，元组等，但字典是无序数据结构，因此解包时必须每个变量名与字典中的键相对应
# 解包元组
my_tuple = (1, 2, 3)
x, y, z = my_tuple
print(x)  # 输出 1
print(y)  # 输出 2
print(z)  # 输出 3

# 解包列表
my_list = [4, 5, 6]
a, b, c = my_list
print(a)  # 输出 4
print(b)  # 输出 5
print(c)  # 输出 6

# 解包字符串
my_string = "hello"
p, q, r, s, t = my_string
print(p)  # 输出 h
print(q)  # 输出 e
print(r)  # 输出 l
print(s)  # 输出 l
print(t)  # 输出 o

# 解包时忽略某些元素
x, _, z = (1, 2, 3)  # 使用 _ 占位符来忽略某个元素
print(x)  # 输出 1
print(z)  # 输出 3

# 解包可变数量的元素
my_tuple = (1, 2, 3, 4, 5)
first, *middle, last = my_tuple  # 使用 * 来解包可变数量的元素
print(first)   # 输出 1
print(middle)  # 输出 [2, 3, 4]
print(last)    # 输出 5


# Dictionary 字典
# 字典（Dictionary）是 Python 中的一种数据结构，用于存储键值对（key-value pairs）。
# 它是一种可变（mutable）的、无序（unordered）的、可迭代（iterable）的集合。
# 在字典中，每个键都与一个值相关联，形成键值对。
# 键必须是唯一的，而值则可以是任何数据类型，包括整数、浮点数、字符串、列表、元组、甚至是其他字典等。
# 字典使用大括号 {} 来表示，每个键值对之间用逗号 , 分隔。

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# 字典的特点包括：
'''
1. 无序性（Unordered）：字典中的键值对没有固定的顺序，因此无法通过索引来访问它们。字典中的键是唯一的，但值可以重复。

2. 可变性（Mutable）：字典是可变的，可以添加、删除或修改键值对。这使得字典成为一个灵活且功能强大的数据结构。

3. 键的唯一性（Uniqueness of keys）：字典中的键必须是唯一的。如果尝试使用相同的键多次对字典进行赋值，最终只会保留最后一次的赋值。

4. 可迭代性（Iterable）：字典可以被迭代，允许你使用循环来遍历字典中的键或值，或者同时遍历键值对。

5. 灵活性（Flexibility）：字典是一种非常灵活的数据结构，可以用于各种场景，如存储配置选项、表示数据库记录、管理数据等。
'''

words = input('> ')
message = words.split(" ")
emoji = {
    ":)":"😊",
    ":(":"😒",
}
output= ""
for word in message:
    output += emoji.get(word,word) + " "
print(output)

emoji.get(word,word) # 一个字典方法调用，它有两个参数：word 是键，word 是默认值。.get() 方法允许你安全地从字典中获取值，即使键不存在也不会导致程序出错，而是返回一个默认值。


# def 自定义函数
# 当你编写 Python 代码时，可能会遇到一些需要重复执行的操作。
# 为了避免代码重复和提高代码的可维护性，你可以将这些操作封装到一个函数中。这个函数可以接受输入参数，并执行特定的操作，然后返回结果。
def function_name(parameter1, parameter2):
    # 函数体，执行特定的操作
    # 可以使用参数来操作数据
    # 可以使用 return 语句返回结果

 '''
 def：这是定义函数的关键字，它告诉 Python 解释器接下来要定义一个函数。
function_name：这是函数的名称，你可以为函数指定一个有意义的名称，用于在代码中调用函数。
(parameter1, parameter2, ...)：这是函数的参数列表，可以接受任意数量的参数，也可以没有参数。这些参数是函数在执行时所需要的输入。
函数体：函数体包含了函数要执行的代码，这是函数的主要部分。在函数体内部，你可以执行各种操作，包括对参数的处理、计算、条件判断、循环等。
return 语句：return 语句用于将结果返回给函数的调用者。它可以是一个值、一个变量、一个表达式，甚至是一个复杂的数据结构。当函数执行到 return 语句时，它会立即终止，并将结果返回给调用者。
 '''

def add_numbers(a, b):
    sum = a + b
    return sum

result = add_numbers(3, 5)
print("The sum is:", result)

# 将以下例子定义为一个函数
# 需要注意的是，任何聊天软件都不需要担心“输入，输出”
'''
words = input('> ')
message = words.split(" ")
emoji = {
    ":)":"😊",
    ":(":"😒",
}
output= ""
for word in message:
    output += emoji.get(word,word) + " "
print(output)
'''

def output(message):
    words = message.split(" "),
    emoji = {
        ":)": "😊",
        ":(": "😢"
    }
    out = ""
    for word in words:
        out += emoji.get(word, word) + " "
        return out


message = input("> ")
result = output(message)
print(result)

