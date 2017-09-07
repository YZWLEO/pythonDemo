#!/usr/bin/python
#coding=utf-8
"""
mysql
"""
import mysql.connector
config = {
    'host':'127.0.0.1',
    'user':'root',
    'port':3306,
    'database':'xiaojinku',
    'password':'',
    'charset':'utf8'
}
try:
    conn = mysql.connector.connect(**config)
except mysql.connector.Error as e:
    print 'connet fails! {}'.format(e)

cursor = conn.cursor();
#cursor.execute("select admin_id,admin_name,created from admin")
rows = cursor.execute("select * from admin")
#print cursor.fetchall
#method 1
# for(admin_id,admin_name,created)in cursor:
#     print"{},{}".format(admin_id,admin_name,created)
#method 2
# for item in cursor:
#     print"{},{},{}".format(*item)


# for item in cursor:
#     print"{0},{1},{2}".format(*item)
#method 3
keys = ['admin_id','admin_name','password','status','created']
for item in cursor:
    map = zip(keys,item);
    #print map
    kv = dict(map)
    #print kv;

    print"{admin_id},{admin_name},{created}".format(**kv)


cursor.close()
conn.close()



