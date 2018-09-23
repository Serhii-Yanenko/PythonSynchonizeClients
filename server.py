import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    _bIsFirstClientDone = False
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address))
        print(self.data)
        # just send back the same data, but upper-cased
        #self.request.sendall(self.data.upper())
        print(MyTCPHandler._bIsFirstClientDone)
        if(str(self.data).find("client 1")!=-1):
            self.request.sendall(b'do step 1')
            data = self.request.recv(1024).strip()
            if(str(data).find("done")!=-1):
                MyTCPHandler._bIsFirstClientDone = True
                print("1st client is done!")
        elif( str(self.data).find("client 2")!=-1):
            if(MyTCPHandler._bIsFirstClientDone == True):
                self.request.sendall(b'do step 2')
                data = self.request.recv(1024).strip()
                if(str(data).find("done")!=-1):
                    print("Finished!")
                    MyTCPHandler._bIsFirstClientDone = False
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