#!/usr/bin/python
# coding=utf-8
class Student:
    __slots_ = ('name','age')



s = Student()
s.name = 'leo'
s.age = 20
print dir(s)
print s.name