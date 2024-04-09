# 列表 
'''
列表(list)是一种基本的数据结构,用于存储序列化的数据项集合。列表是可变的(mutable),
这意味着它们的内容可以在创建后被修改。列表可以包含不同类型的元素，包括数字、字符串、
甚至其他列表（这称为嵌套列表）。列表是用方括号 [] 表示，元素之间用逗号 , 分隔。
'''
my_list = [1, "Hello", 3.14]
print(my_list[0])  # 输出：1
print(my_list[1])  # 输出："Hello"
my_list[1] = "Python"
print(my_list)  # 输出：[1, "Python", 3.14]
my_list.append("new")
print(my_list)  # 输出：[1, "Python", 3.14, "new"]

# 函数接受输入的内容，并打印出来
print(convert_to_snake_case('aLongAndComplexString'))

# 这段代码定义了一个函数'convert_to_snake_case'，其目的是将给定的pascal/camel字符串转化为snake_case
def convert_to_snake_case(pascal_or_camel_cased_string):
    # snake_cased_char_list = []
    # for char in pascal_or_camel_cased_string:
    #     if char.isupper():
    #         converted_character = '_' + char.lower()
    #         snake_cased_char_list.append(converted_character)
    #     else:
    #         snake_cased_char_list.append(char)
    # snake_cased_string = ''.join(snake_cased_char_list)
    # clean_snake_cased_string = snake_cased_string.strip('_')

    # return clean_snake_cased_string
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
        ]

    return ''.join(snake_cased_char_list).strip('_')


def main():
    print(convert_to_snake_case('aLongAndComplexString'))


if __name__ == '__main__':
    main()

# .upper 和 .isupper
'''
.upper()
.upper() 方法用于将字符串中的所有字母转换为大写。
这个方法不接受任何参数，并返回一个新的字符串，原字符串中的所有小写字母都被转换为了大写字母。
原字符串不会被修改（因为在 Python 中字符串是不可变的）。
'''
original_string = "Hello World"
uppercased_string = original_string.upper()
print(uppercased_string)  # 输出: HELLO WORLD

'''
.isupper()
.isupper() 方法用于检查字符串中的所有字母是否都是大写。
如果字符串至少包含一个字母，并且所有字母都是大写，则这个方法返回 True,否则返回 False。
这个方法也不修改原字符串，它仅仅检查条件并返回一个布尔值。
'''
string1 = "HELLO WORLD"
string2 = "Hello World"

print(string1.isupper())  # 输出: True
print(string2.isupper())  # 输出: False

# .join()
'''
join() 是 Python 中的一个字符串方法，它用于将序列（如列表、元组等）中的元素连接成一个新的字符串，元素之间由 .join() 方法的调用者指定的字符串分隔。
join()只接受一个参数，对于多个字符串，可以先将多个字符串转化为一个列表，然后再使用'.join()'
'''
separator.join(iterable)
# separator 是你希望用来分隔序列元素的字符串。
# iterable 是包含要连接的字符串元素的可迭代对象，如列表、元组等。
# 使用空格作为分隔符
words = ['Hello', 'World', '!']
result = ' '.join(words)
print(result)  # 输出: Hello World !

# 使用逗号加空格作为分隔符
words = ['apple', 'banana', 'cherry']
result = ', '.join(words)
print(result)  # 输出: apple, banana, cherry

# 使用空字符串作为分隔符
letters = ['P', 'y', 't', 'h', 'o', 'n']
result = ''.join(letters)
print(result)  # 输出: Python

'''
.join() 方法对 iterable 中的每个元素调用了 str()，所以即便元素不是字符串类型，它也会尝试将它们转换为字符串。如果转换失败，会抛出异常。
如果 iterable 中包含任何非字符串类型（且无法通过 str() 转换为字符串的），.join() 方法将引发 TypeError。
.join() 是处理字符串连接操作的高效方法，尤其是在涉及到大量字符串时，使用 .join() 方法比使用 + 运算符连接字符串要高效得多。
这是因为在 Python 中，字符串是不可变的，使用 + 运算符连接字符串时会频繁创建和销毁对象，而 .join() 方法只创建一个新字符串。
'''

# strip
'''
.strip()
.strip() 是 Python 中字符串(str 类型)的一个方法，它的功能是移除字符串两端（开头和结尾）的空白字符，包括空格、制表符 (\t)、换行符 (\n) 等。它非常有用于清理字符串数据。
'''
# 当 .strip() 不带参数时，它默认移除字符串两端的所有空白字符：
text = "   Hello World!   "
cleaned_text = text.strip()
print(cleaned_text)  # 输出: "Hello World!"

# .strip() 也可以接受一个字符串参数
text = "xxHello World!xx"
cleaned_text = text.strip('x')
print(cleaned_text)  # 输出: "Hello World!"

'''
.strip() 方法仅影响字符串的开头和结尾，不会改变字符串中间部分的任何字符。
与所有字符串方法一样，.strip() 返回一个新的字符串，原字符串不会被修改，这是因为 Python 中的字符串是不可变的。
'''