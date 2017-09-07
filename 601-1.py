#!/usr/bin/python
# -*- coding: UTF-8 -*-
# print text

def fab(max):
    n,a,b = 0,1,1;
    #print n,a,b,"\r\n"
    while n<max:
        #print n, a, b, "\r\n"
        #print b
        yield b;
        a,b = b,a+b;
        n = n+1

list = fab(5)
for n in list:
    print n