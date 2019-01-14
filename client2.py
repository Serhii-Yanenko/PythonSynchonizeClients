import socket
import sys
import time
def client2(n):
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
        if(str(received).find("do step "+str(n))!=-1):
            print("do script "+str(n))
            for i in range(0, 10):
                time.sleep(1)
                print("*")
            done_data = "step "+str(n)+" done"
            sock.sendall(bytes(done_data,"utf-8"))
            print(done_data)
            return True
        elif(str(received).find("wait")!=-1):
            print("wait for client 1 complete before step - "+str(n))
            sock.sendall(b'wait')
            return False
        else:
            print("Bad request")
            return False
def main():
    bIsDone = False
    while(bIsDone == False):
        bIsDone = client2(2)
        #time.sleep(1)

    bIsDone = False
    while(bIsDone == False):
        bIsDone = client2(4)
        #time.sleep(1)
     
    print("done!")

if __name__ == "__main__":
    main()
