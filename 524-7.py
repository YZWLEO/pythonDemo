#coding=utf-8
import io
try:
    fh = open('a.txt','w')
    fh.write("测试")
    pass
except IOError:
    print "没有找到"
    pass
else:
    print "ok"
    fh.close()
