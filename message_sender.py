import socket

ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host  = "192.168.1.131"
port  = 8888
ainfo =  socket.getaddrinfo(host, port)
print(ainfo)
print(ainfo[0][4])
ms.connect(ainfo[0][4])
ms.sendall(b"Hello workl")
ms.close()

