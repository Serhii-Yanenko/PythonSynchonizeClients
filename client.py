import socket
import sys
def client1():
    HOST, PORT = "localhost", 9999
    data = "client 1"

    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n", "utf-8"))

        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")

        print("Sent:     {}".format(data))
        print("Received: {}".format(received))
        if(str(received).find("do step 1")!=-1):
            print("Run script 1")
            sock.sendall(b'done')
if __name__ =="__main__":
    client1()