import socket

HOST = '127.0.0.1'
PORT= 50008

global sock
global connectedSock

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORT))
print("server name: ", sock.getsockname())
sock.listen(1)
connectedSock, addr = sock.accept()
print("client name: ", addr)


while True: 
    data = connectedSock.recv(4096)
    if not data:
            break
    print(data)
    
