python语法和linux命令以及R命令不一样，在区分大小写的同时，也要区分"空格"，否则python程序无法运行
ps：python会要求这么写
class User(object):
pass


if __name__=='__main':
print(dir(User()))
只有当函数被识别（字体颜色改变），语法才是正确的

2)  区分单引号，双引号，三引号的作用
单引号用来表示一整句话，PS：它来自非洲大草原。
str='它来自非洲大草原'
print(str)
双引号用来强调某个单词，PS：它来自'非洲'大草原
str="它来自'非洲'大草原"
print(str)
三引号用来表示说话的语句，PS： 他说："它来自非洲大草原！"
str='''他说："它来自非洲大草原！"'''
print(str)
单引号也可以用'\''代替，双引号则是"\""
str1="它来自\'非洲\'大草原"
str2="他说：\"它来自非洲大草原！\""
print(str1)
print(str2)

# 列表(list)与元组(tuple)
# 列表
list=['两点水','三点水','sidianshui']
# 元组
tuple=('两点水','三点水','sidianshui')
# 列表与元组的区别在于
列表可以后续更改
元组一旦创建后，不能更改
而且在创建列表时，使用中括号【】
元组使用小括号（）
# 当你想查询一个变量是否是元组时，使用type函数或isinstance
print(type(list))
if isinstance(list,tuple):
print('list 是一个元组')

# 字典与set
字典----dict
name ={'一点水':'45632189563','两点水':'753214896325'}
dict 使用花括号'{}'创建
字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
dict = {key1 : value1, key2 : value2 }


# 自定义函数
# 函数组成
def 函数名(参数1，参数2....参数n):
    函数体
    return 语句

# 以自定义函数，基本有以下规则步骤：

    函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()
    任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数
    函数的第一行语句可以选择性地使用文档字符串（用于存放函数说明）
    函数内容以冒号起始，并且缩进
    return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的 return 相当于返回 None。

# 语法示例:
def functionname( parameters ):
   "函数_文档字符串"
   function_suite
   return [expression]

# 实例

def sum (num1,num2):
    '两数之和'
    return num1+num2

sum(5,9)
print(sum(5,9))

# 在Python中，% 和 / 是两个不同的操作符，分别表示不同的含义：

    %：取余操作符
        % 用于计算两个数相除后的余数。例如，a % b 表示将 a 除以 b 并返回余数部分。
        例如，9 % 4 返回1，因为9除以4的余数是1。

    /：除法操作符
        / 用于执行两个数的除法操作，返回结果为一个浮点数（除非使用 // 进行整数除法）。
        例如，9 / 4 返回2.25，因为9除以4等于2.25。

# python 中输出的结果连接很紧密
# 比如：昵称:龙傲天年龄:18性别:女
# 我们想让'龙傲天'与'年龄'隔开，龙傲天   年龄
# 可以将   end= '     '          隔开
# python
def print_user_info(name,age,sex='男'):
    #打印用户信息
    print( '昵称:{}'.format(name)  ,  end='  ')
    print( '年龄:{}'.format(age)  ,  end='  ')
    print( '性别:{}'.format(sex))
    return;

print_user_info( '龙傲天'  ,  18  ,  '女'  )