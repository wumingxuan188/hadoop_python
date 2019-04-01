import socket
# 创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口
s.bind(("127.0.0.1", 9999))
# 开启监听
s.listen(0)
print("监听启动了")
while True:
    (ss,adrr) = s.accept()
    while True:

        data = ss.recv(1024)
        print(data)
        print(data.decode("utf-8"))

