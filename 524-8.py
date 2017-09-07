#!/usr/bin/python
#coding=utf-8
"""
面向对象
"""

class Employee:
    '员工基类'
    empCount = 0
    def __init__(self,name ,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        pass
    def displayCount(self):
        print "total emploee {}".format(Employee.empCount)
        pass

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary


user = Employee(name="leo",salary='1')
print user.__class__
print user.__doc__
print user.displayCount()
print user.displayEmployee()
e1 = Employee('a','1')
print e1.displayCount()
print Employee.__dict__
print Employee.__name__
print Employee.empCount