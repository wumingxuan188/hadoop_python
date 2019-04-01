import socket
sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender.bind(("127.0.0.1",9999))
index = 0
while index < 100:
    data = "hello:udp"+str(index)
    sender.sendto(data.encode("utf-8"),("127.0.0.1",8888,))
    index+=1
    recv = sender.recv(1024)
    print(recv.decode("utf-8"))
    import time
    time.sleep(2)
