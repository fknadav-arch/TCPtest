import socket
import threading

HOST = '0.0.0.0'
PORT= 50008

def recive (listening_sock):
    try:
        while True:
            dataIn = listening_sock.recv(4096)
            if not dataIn:
                print("client disconnected")
                break
            try:
                print ("in: ", dataIn.decode('utf-8'))
            except UnicodeDecodeError:
                print("recived invalid UTF-8 data")
            
    except ConnectionResetError:
        print("client disconnected unexpectedly")
    finally:
        listening_sock.close()

def send_to (connected_sock):
    try:
        while True:
            data_out = input()
            print("out: ", data_out)
            connected_sock.sendall(data_out.encode('utf-8'))
            if data_out == "exit":
                break
    except (BrokenPipeError, ConnectionResetError, OSError):
        print("client is no longer connected")
    finally:
        connected_sock.close()

def main ():

    listening_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listening_sock.bind((HOST,PORT))
    listening_sock.listen(1)
    print("listening")

    connected_sock, addr = listening_sock.accept()
    print("client name: ", addr)

    recv_thread = threading.Thread(target=recive, args=(connected_sock,), daemon=True)
    send_thread = threading.Thread(target=send_to, args=(connected_sock,), daemon=True)

    recv_thread.start()
    send_thread.start()

    recv_thread.join()
    send_thread.join()


if __name__ == "__main__":
    main()


