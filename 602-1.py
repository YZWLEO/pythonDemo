#!/usr/bin/python
# coding=utf-8
import functools
__author__ = 'leoyan'

int2 = functools.partial(int,base=2)
print int2('1000000')