name = ['两点水','sandianshui','四点水',123,'sjhyiul','阿水']
print(name)

print(name[2])
print(name[0:2])
print(name[1])
print(name[:2])
print(name[:])
print(name[3])
print(name[-2])
print(name[1:2])
print(name[0:1])
print(name[1:3])
print(name[0:3])

name[1]='一点水'
print(name)
name[1] = '一点水'
print(name)

name = ['一点水','两点水','三点水','四点水','五点水']
name[1]='2点水'
print(name)
name.append('六点水')
print(name)
del(name[3])
del name[3]
print(name)
len(name)

User=['两点水','towdater','两点水','yidianshui']
print('1.产品用户')
print(User)

len(User)
print('\n2,统计有多少用户')
print(len(User))
print('\n3.具体用户')
print(User[0]+','+User[1]+','+User[2])
print(User[0]+','+User[1]+','+User[2]+','+User[3])
User.append('五点水')
print(User)
User.insert(0,'VIP')
print(User)
del User[4]
print('\n4.VIP 用户')
print(User)

User.pop(4)
print(User)

User[1] = '2点水'
print(User)
newuser=[['VIP',1111],['两点水',2222],['三点水',3333]]
print('\n5.用户与帐号信息')
print(newuser)
print(type(newuser))

ser=('两点水','三点水','四点水')
if isinstance(ser,tuple):
    print('ser 是一个元组')

list1=['123','456']
tup1=('两点水','三点水',456,523,list1)
print(list1)
print(tup1)

list1[1]='789'
print(tup1)

del tup1
print(tup1)

name1=('一点水','两点水','sandianshui','四点水')
name2=('1点水','2点水','3点水','4点水')
list=['一点水','两点水','三点水','四点水']

print(len(name1))
print(name1+name2)
print(name1*2)
print(max(name2))
print('一点水' in name1)
print(tuple(list))



    