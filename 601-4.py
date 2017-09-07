#!/usr/bin/python
# coding=utf-8
x = abs(-10)

print x
f = abs
print f(-99)


def pingfang(x):
    return x*x

r = map(pingfang,[1,2,3,4,5,6,7])
print r;

def add(x,y):
    return x*10+y;

print reduce(add,[1,3,5,7,9])
#print map(add,[1,3,5,7,9])

fb = lambda x,y:x*y
print fb;
print fb(10,9)