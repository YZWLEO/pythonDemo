#!/usr/bin/python
#coding=utf-8
"""
正则
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

import re
print re.match('www','www.chinacloud.com').span()
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配