import socket
import sys
import time
def client2():
    HOST, PORT = "localhost", 9999
    data = "client 2"

    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n", "utf-8"))

        # Receive data from the server and shut down
        #received = str(sock.recv(1024), "utf-8")

        print("Sent:     {}".format(data))
        
    
        received = str(sock.recv(1024), "utf-8")
        print("Received: {}".format(received))
        if(str(received).find("do step 2")!=-1):
            print("do script 2")
            sock.sendall(b'done')
            return True
        elif(str(received).find("wait")!=-1):
            print("wait for client 1 complete")
            sock.sendall(b'wait')
            return False
        else:
            print("Bad request")
            return False
def main():
    bIsDone = False
    while(bIsDone == False):
        bIsDone = client2()
        time.sleep(10)
    print("done!")

if __name__ == "__main__":
    main()
