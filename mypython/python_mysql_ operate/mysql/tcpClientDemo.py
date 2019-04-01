import socket
# 创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接地址
s.connect(("127.0.0.1",9999))
index = 0
while index < 100:
    b="hello"+str(index)
    s.send(b.encode("utf-8"))
    index += 1
    import time
    time.sleep(2)
