import socket
import sys
import time
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
            for i in range(0, 10):
                time.sleep(1)
                print("*")
            print("script 1 i done")
            sock.sendall(b'step 1 is done')


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        bIs2ndRoundDone = False
        while(bIs2ndRoundDone == False):
            sock.sendall(bytes(data + "\n", "utf-8"))
            
            received = str(sock.recv(1024),"utf-8")
            if(str(received.find("do step 3")!=-1)):
                print("step 3")
                for i in range(0, 10):
                    time.sleep(5)
                    print("*")
                print("step 2 is done!\n")
                bIs2ndRoundDone = True
                sock.sendall(b'step 2 is done!')
            else:
                print("wait client 2 complete! ")


if __name__ =="__main__":
    client1()