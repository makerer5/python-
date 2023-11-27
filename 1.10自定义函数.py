def sum (num1,num2):
    '两数之和'
    return num1+num2

sum(5,9)
print(sum(5,9))

def  sum (num1,num2):
    #两数之和
    if  not (isinstance(num1,(int,float))  and  isinstance(num2,(int,float))):
        raise TypeError('参数类型错误')
    return num1+num2
    
sum(1,2)
print(sum(1,2))

sum('两点水',2)

def division (num1,num2):
    #余商和余数
    a = num1 % num2
    b = (num1-a)/num2
    return b,a

division(9,4)
a = 9%4
b = (9-a)/4
print(a)
print(b)

num1,num2=division(9,4)
tuple = division(9,4)
print(num1,num2)
print(tuple)

tuple=(5,2)
print(tuple)

tuple[1]
tuple[0]
del tuple
print(tuple)

list1=[123,7890]
tup1=(123,'两点水',756,'三点水',list1)
print(tup1)

list1[0]=5623
print(tup1)

del tup1
print(tup1)

def print_user_info(name,age,sex='男'):
    #打印用户信息
    print( '昵称:{}'.format(name)  ,  end='  ')
    print( '年龄:{}'.format(age)  ,  end='  ')
    print( '性别:{}'.format(sex))
    return;

print_user_info( '龙傲天'  ,  18  ,  '女'  )
print_user_info('高天',24)












