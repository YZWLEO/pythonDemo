#!/usr/bin/python
#coding=utf-8
"""
面向对象  继承
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
    def __init__(self):
        print "子类构造"

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