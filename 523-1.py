#coding=utf-8
list = [1,2,3];
list2=[3,4,5,3,4,5,6,7,5,5,5];
print list+list2
print list*3
print list2.count(4)
list.extend(list2)
print list
print list.index(3)
print list2.index(5)
list.insert(20,99)
print list
print list.pop(-1)
print list