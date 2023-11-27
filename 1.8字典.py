name={'一点水':'1546893','两点水':'4567823156','三点水':'4562314789'}
print(name['三点水'])

name['jack']='4567823156'
print(name)

name['一点水']='123456789'
print(name)

del name['jack']
print(name)

name.clear()
print(name)

del name
print(name)

print(name)

set1=set([123,456,789])
print(set1)

list=[123,456,123,789,852,852]
set2=set(list)
print(set2)

set2.add('两点水')
print(set2)

set2.remove('两点水')
print(set2)

set1=set('hello')
set2=set(['h','y','y','o','n','m'])
print(set1)
print(set2)
set3=set1 & set2
print('\n交集 set3:')
print(set3)

set4=set1 | set2
print('\n并集 set4:')
print(set4)

set5=set1 - set2
set6=set2 - set1
print(set5)
print(set6)

