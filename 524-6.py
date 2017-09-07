#coding=utf-8
import io
# str = raw_input("请输入")
# print "i输入的是",str
# print "ni 输入的是 {}".format(raw_input("请input"))

object = open("524-3.py",'rb')
print object
print object.closed
object.close()
print object.closed
print globals()
print locals()

