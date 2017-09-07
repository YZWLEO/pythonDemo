#!/usr/bin/python
# coding=utf-8
import urllib2,cookielib
# response = urllib2.urlopen('http://www.baidu.com')
# print response.getcode()
# print response.read()

def func(n):
    return 1 if n == 0 else n*func(n-1)


print func(5)
#120

def capitaliza_all(t):
    return [s.capitalize() for s in t]


print capitaliza_all(('a','b'))
print capitaliza_all(['a','b','c'])

print sum([1,2,3,4,5])

a = b = 6
b2 = 6

print a is b
print b is b2
c = d = [1,2,3]
e = [1,2,3]
print c is d
print c is e
print set({1:1,2:20,3:3})-set({1:1,3:4,5:5})

k = {1:1,2:20,3:3};
h = {1:1,3:4,5:5};
print set(k).difference(h)