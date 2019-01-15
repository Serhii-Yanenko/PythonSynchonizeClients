import socket
import sys
import time
def client1(n):
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
        if(str(received).find("do step "+str(n))!=-1):
            print("Run script 1")
            for i in range(0, 10):
                time.sleep(1)
                print("*")
            print("script 1 i done")
            sock.sendall(b'step 1 is done')

def client1_step2():
    HOST, PORT = "localhost", 9999
    data = "client 1"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        
        bIs2ndRoundDone = False
        while(bIs2ndRoundDone == False):
            print("send data to socket "+str(data))
            #sock.connect((HOST, PORT))
            try:
                sock.connect((HOST, PORT))
                sock.sendall(bytes(data + "\n", "utf-8"))
            
                received = str(sock.recv(1024),"utf-8")
                print(received)
                if(received.find("do step 3")!=-1):
                    print("step 3")
                    for i in range(0, 10):
                        time.sleep(5)
                        print("*")
                    print("step 2 is done!\n")
                    bIs2ndRoundDone = True
                    sock.sendall(b'step 2 is done!')
                    print(str(sock.recv(1024),"utf-8"))
                    sock.shutdown(0)
                else:
                    print("wait client 2 complete! ")
            except:
                print("connection is abourted!")
                

            #sock.shutdown()
        
def client2(n):
    HOST, PORT = "localhost", 9999
    data = "client 1"

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
if __name__ =="__main__":
    client1(1)
    bIsDone = False
    while(bIsDone == False):
        bIsDone = client2(3)
        time.sleep(2)