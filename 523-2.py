#coding=utf-8
dic = {'name':"leo","age":200,"sex":'m'}
print dic
del dic['name']
print dic
dic.clear()
print dic
import time
ticks = time.time()
print ticks;
localtime = time.localtime(time.time())
print "本地时间为 :",localtime
localtime = time.asctime( time.localtime(time.time()) )
print "本地时间为 :", localtime