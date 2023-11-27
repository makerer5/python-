results=59
if results>=60:
    print('及格')
else:
    print('不及格')

num = ''
if num:
    print('hello python')
else:
    print('hello world')

results = 89
if results>= 90:
    print('优秀')
elif results>= 80:
    print('良好')
elif results>= 60:
    print('及格')
elif results<=59:
    print('不及格')

java = 86
python = 68
if  java > 80 and python > 80:
    print('优秀')
else:
    print('良好')
if (java>80 and python >80) or (java> 80 and python < 90):
    print('优秀')
else:
    print('及格')

if java>= 80:
    if python>=90:
        print('优秀')
    else:
        print('不优秀')
else:
    print('及格')

for letter in '两点水 hello':
    print(letter)

dict={'一点水':'小学生','两点水':'初中生','三点水':'高中生'}
for i in dict:
    print(i)

list=[123,456,789,'一点水']
for i in list:
    print(i)

tuple=(123,456,789,'三点水')
for i in tuple:
    print(i)

set1=set(list)
for i in set1:
    print(i)

    results= 91
    for i in results:
        print(i)

b= 0.65
for i in b:
    print(i)

for i in range(3):
    print(i)

for i in range(0,3):
    print(i)

for i in range(2,9,2):
    print(i)

couunt =1
sum1=0
while couunt<= 100:
    sum1 = sum1+ couunt
    couunt= couunt + 1
print(sum1)

i = 0
while i < 100:
    i = i +1
print(i)

for i in range(0,100):
    print(i)

count= 0
sum = 1
while (count<= 100):
    sum = count+sum
    count = count+1
    if (sum>=1000):
        break
print(sum)

for i in range(0,100,2):
    print(i)

count =0
sum =1
while (count<=100):
    if (count %2 ==0):
        count = count+1
        continue
    sum=sum+count
    count=count+1
print(sum)
for num in range(10,20):
    for i in range(2,num):
        if num%i ==0:
            j=num/i
            print('%d 是一个合数' % num)
            break
    else:
        print('%d 是一个质数' % num)

for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(i, j, i*j), end='')
    print()

year = int(input(2023))
if (year % 4 ==0 and (year %100))  !=0 or (yead % 400)==0 :
    print('{0} 是一个闰年'.format(year))
else:
    print('{0}'.format(year))



















