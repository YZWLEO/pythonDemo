#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import json
# jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
# text = json.loads(jsonData)
# print text

import demjson
a = {'a':'a','name':'wei'}
b = demjson.encode(a)
print b
test = [1,2,3,4,5,'6']
print demjson.encode(test)

a = range(1,5)
print a
count = 0;
for i in a:
    for j in a:
        for k in a:
            if (i!=j) and (i!=k) and (j!=k):
                print "{},{},{}".format(i,j,k)
                count += 1;
                pass

print "Total",count