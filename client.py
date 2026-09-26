import socket
import threading

HOST = '127.0.0.1'
PORT= 50008

def recive (connected_sock):
    try:
        while True:
            dataIn = connected_sock.recv(4096)
            if not dataIn:
                print("server disconnected")
                break
            print ("in: ", dataIn.decode('utf-8'))
    except ConnectionResetError:
        try:
            print ("in: ", dataIn.decode('utf-8'))
        except UnicodeDecodeError:
            print("recived invalid UTF-8 data")
    finally:
        connected_sock.close()

def send (connected_sock):
    while True:
        try:
            dataOut = input()
            print("out: ", dataOut)
            connected_sock.sendall(dataOut.encode('utf-8'))
        except (BrokenPipeError, ConnectionResetError, OSError):
            print("server is no longer connected")
            connected_sock.close()
            break

def main():
    connected_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected_sock.connect((HOST,PORT))
    recv_thread = threading.Thread(target = recive, args= (connected_sock,), daemon=True)
    send_thread = threading.Thread(target = send, args= (connected_sock,), daemon=True)

    recv_thread.start()
    send_thread.start()

    recv_thread.join()
    send_thread.join()

if __name__ == "__main__":
    main()