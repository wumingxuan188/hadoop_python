import MySQLdb
"""#开连接
connect = MySQLdb.Connect("localhost", "root", "root", "wmx")
# 打开游标
cur = connect.cursor()
# sql语句
sql = "insert into hadoop_user(name, age) values ('tom1',18)"
# 执行语句
cur.execute(sql)
# 提交事务
connect.commit()
# 关闭连接
connect.close()
"""
'''
# 批量增加
connect = MySQLdb.connect("127.0.0.1", "root", "root", "wmx")
cur = connect.cursor()
i = 0

while i < 10000:
    sql = "insert into hadoop_user(name,age) values ('%s',%d )" % ("tom"+str(i) , i % 100)
    print(sql)
    cur.execute(sql)
    connect.commit()
    i = i+1
connect.close()
'''
# 查询
connect = MySQLdb.connect("localhost", "root", "root", "wmx")
cur = connect.cursor()
sql = "select * from  hadoop_user"
cur.execute(sql)
data = cur.fetchall()
for i in data:
    print(i[0])
    print(i[1])
    print(i[2])

connect.commit()
connect .close()