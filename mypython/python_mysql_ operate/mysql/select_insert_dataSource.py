import MySQLdb

'''
测试手动开启事务
'''
# connect = MySQLdb.connect("localhost", "root", "root", "wmx")
# try:
#     # 开闭自动提交
#     connect.autocommit(False)
#     # 开启事务
#     connect.begin()
#     # 打开游标
#     cur = connect.cursor()
#     sql = "delete from hadoop_user where id > 1000 "
#     cur.execute(sql)
#     # 提交事务
#     connect.commit()
#     # 关闭游标
#     cur.close()
# except Exception:
#     connect.rollback()
# finally:
#     connect.close()

"""
测试调用函数
"""

conn = MySQLdb.connect("localhost", "root", "root", "wmx")
try:
    conn.autocommit(False)
    conn.begin()
    cur = conn.cursor()
    sql = "select sf_add(1,5)"
    cur.execute(sql)
    # 查找结果
    data = cur.fetchone()
    print(data[0])
    conn.commit()
    cur.close()
except Exception:
    conn.rollback()
    print("挂了")
finally:
    conn.close()


