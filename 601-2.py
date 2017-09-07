#!/usr/bin/python
# -*- coding: UTF-8 -*-
# print text


def user_loggin(func):

    def wrapper():
        print "{} is running".format(func.__name__)
        return func();
    return wrapper()

@user_loggin
def foo():
    print "i am foo"


foo();

@user_loggin
def foo2():
    print "i am foo2"


#foo()

#foo  = user_loggin(foo)

#foo2()

