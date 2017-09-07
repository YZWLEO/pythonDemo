#!/usr/bin/python
# coding=utf-8

# import os
# print os.sys.path
# print os.sys.platform
import requests
# r = requests.get('https://github.com/YZWLEO/webUploaderDemo/blob/master/README.md')
# #print r.text;
# print r.url;
# print r.request
# print r.encoding
# print r.content

r = requests.post("http://www.baidu.com",{'key1':'vaule1','key2':'value2'})
print r.status_code
print r.headers
print requests.codes.ok
print r.cookies
print r.history