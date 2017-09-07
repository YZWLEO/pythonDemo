#!/usr/bin/python
#coding=utf-8
"""
面向对象   私有变量  公共变量
"""

class Parent:
    parentAttr = 100
    def __init__(self):
        print "父类构造"

    def parentMethod(self):
        print "弗雷方法"

    def setAtrr(self,attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "弗雷属性",Parent.parentAttr

class Child(Parent):
    __age = 0
    count = 0;
    def __init__(self):
        print "子类构造"
        self.__age += 1
        self.count += 1

    def childMethod(self):
        print "子类方法"
        pass

c = Child()
c.childMethod()
c.parentMethod()
c.setAtrr(200)
c.getAttr()
print issubclass(Child,Parent)
print isinstance(c,Child)
print isinstance(c,Parent)

print c.count
#print c.__age
print '#',c._Child__age
print vars(c)
print vars(Child)
print Child.__dict__