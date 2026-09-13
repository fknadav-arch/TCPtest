import socket
import threading

HOST = '127.0.0.1'
PORT= 50008

def recive (sock):
    while True:
        dataIn = sock.recv(4096)
        print ("in: ", dataIn.decode('utf-8'))


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))
sock.sendall(b'Hello World')
recvTh = threading.Thread(target = recive, args= (sock,), daemon=True)
recvTh.start()
while True:
    dataOut = input()
    print("out: ", dataOut)
    sock.sendall(dataOut.encode('utf-8'))
