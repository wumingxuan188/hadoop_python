#导入thrift的python模块
import os
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


# 导入自已编译生成的hbase python模块
from mythrift.hbase import THBaseService
from mythrift.hbase.ttypes import *
from mythrift.hbase.ttypes import TResult

# 创建socket连接
t_socket = TSocket.TSocket('s201', 9090)
transport = TTransport.TBufferedTransport(t_socket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = THBaseService.Client(protocol)
# 打开传输端口
transport.open()


"""
put操作
"""
"""
# 表名
tableName = b"ns1:t1"
# 行id
row = b"row6"
# 列名称和值
v1 = TColumnValue(b"f1", b"id", b"101")
v2 = TColumnValue(b"f1", b"name", b"tom")
v3 = TColumnValue(b"f1", b"age", b"24")
#
vls = [v1, v2, v3]
# 放在行中
t_put = TPut(row, vls)
# 放在表中
client.put(tableName,t_put)
print("okkkk")
transport.close()

"""
"""
get操作
"""
'''
tableName = b"ns1:t1"
rowKey = b"row12"
col1 = TColumn(b"f1",b"id")
col2 = TColumn(b"f1", b"name")
col3 = TColumn(b"f1",b"age")
cols = [col1,col2,col3]
t_get = TGet(rowKey, cols)
res = client.get(tableName,t_get)
# print(res.columnValues[0])
# print("===============================")
# print(res.columnValues[1])
# print(res.columnValues[2])

for x in res.columnValues:
    print(bytes.decode(x.family))
    print(bytes.decode(x.qualifier))
    print(bytes.decode(x.value))
    print("======================")
'''
'''
delete操作
'''
"""
tableName = b"ns1:t1"
rowKey = b"row12"
col2 = TColumn(b"f1", b"name")
col3 = TColumn(b"f1",b"age")
cols = [col2,col3]
# 创建删除对象
t_delete = TDelete(rowKey, cols)
client.deleteSingle(tableName,t_delete)
transport.close()
print("delete ok")
"""
"""
全表扫描
"""
tableName = b"ns1:t1"
rowKey = b"row12"
t_scan = TScan()
results = client.getScannerResults(tableName, t_scan,100)
for x in results:
    print(x.row)
    print(x)
# print(results)
