import socket
rev = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
rev.bind(("127.0.0.1",8888))
while True:
    recv = rev.recv(1024)
    print(recv.decode("utf-8"))
    data="我收到了"
    rev.sendto(data.encode("utf-8")+recv,("127.0.0.1",9999))

