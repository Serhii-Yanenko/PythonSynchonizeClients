import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    _bIsClient1Step1IsDone = False
    _bIsClient2Step1IsDone =False
    _bIsClient1Step2IsDone = False
    _bIsClient2Step2IsDone = False
    def print_parameters(self):
        print(self._bIsClient1Step1IsDone)
        print(self._bIsClient1Step2IsDone)
        print(self._bIsClient2Step1IsDone)
        print(self._bIsClient2Step2IsDone)

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address))
        print(self.data)
        # just send back the same data, but upper-cased
        #self.request.sendall(self.data.upper())
        self.print_parameters()
        if(str(self.data).find("client 1")!=-1):
            if(MyTCPHandler._bIsClient1Step1IsDone == True):
                print("wait until step 2 is implemented by client 2")
                if(MyTCPHandler._bIsClient2Step1IsDone == False):
                    print("wait until step 1 is implemented by client 2")
                    self.request.sendall(b'wait')
                else:
                    self.request.sendall(b'do step 3')
                    data = self.request.recv(1024).strip()
                    if(str(data).find("step 3 done")!=-1):
                        MyTCPHandler._bIsClient1Step2IsDone = True
                        print("1st client is done!")

            else:
                self.request.sendall(b'do step 1')
                data = self.request.recv(1024).strip()
                if(str(data).find("step 1 is done")!=-1):
                    MyTCPHandler._bIsClient1Step1IsDone = True
                    print("1st client is done!")
        elif( str(self.data).find("client 2")!=-1):
            if(MyTCPHandler._bIsClient1Step1IsDone == True):
                if(MyTCPHandler._bIsClient1Step2IsDone == False):
                    self.request.sendall(b'do step 2')
                    data = self.request.recv(1024).strip()
                    if(str(data).find("step 2 done")!=-1):
                        print("Finished 1st round!")
                        MyTCPHandler._bIsClient2Step1IsDone = True
                else:
                    self.request.sendall(b'do step 4')
                    data = self.request.recv(1024).strip()
                    if(str(data).find('done')!=-1):
                        print("Finished 4th script")
                        self._bIsClient1Step1IsDone = False
                        self._bIsClient1Step2IsDone = False
                        self._bIsClient2Step1IsDone = False
                        self._bIsClient2Step2IsDone = False
                        self.print_parameters()
                    else:
                        self.request.sendall(b'wait')
                        self._bIsClient1Step1IsDone = False
                        self._bIsClient1Step2IsDone = False
                        self._bIsClient2Step1IsDone = False
                        self._bIsClient2Step2IsDone = False
                        print("wait for client 1 step 3 complete")

            else:
                self.request.sendall(b'wait')
                print("wait for client 1 complete")
                data = self.request.recv(1024).strip()
                if(str(data).find("wait")):
                    self.request.sendall(b'quit')
            

        
            

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()