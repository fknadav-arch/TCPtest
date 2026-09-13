import socket
import threading

HOST = '127.0.0.1'
PORT= 50008

def recive (sock):
    while True:
        dataIn = sock.recv(4096)
        print ("in: ", dataIn.decode('utf-8'))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORT))
print("server name: ", sock.getsockname())
sock.listen(1)
connectedSock, addr = sock.accept()
print("client name: ", addr)

recvTh = threading.Thread(target = recive, args= (connectedSock,), daemon=True)
recvTh.start()

while True: 
    dataOut = input()
    print("out: ", dataOut)
    connectedSock.sendall(dataOut.encode('utf-8'))
    
