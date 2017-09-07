# -*- coding:utf-8 -*-
import sys
import pymysql.cursors
#print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf8')

config = {
    'host':'172.28.41.201',
    'user':'sq_videochina',
    'port':3306,
    'database':'videochina_goods',
    'password':'videochina@2016',
    'charset':'utf8'
}
conn = pymysql.connect(**config)
cursor = conn.cursor()
print cursor.execute("insert into tb_config(configName,configKey,addTime) values('aaa','bbbb','1410855715')")
#cursor.execute("select * from tb_goods limit 10")
cursor.execute("select * from tb_config where id<10 order by id desc limit 10")
row1 = cursor.fetchone()
key = ['id','configName','configKey','configValue','status','addTime']
print list(zip(key,row1))
print dict(zip(key,row1))
exit()
#
# print row1[1]
# row2 = cursor.fetchall();
# print row2
rows = cursor.fetchall()
for item in rows:
    print "{0},{1},{2},{3},{4},{5}".format(*item)


for item in rows:
    print "{0},{1},{2}".format(*item)