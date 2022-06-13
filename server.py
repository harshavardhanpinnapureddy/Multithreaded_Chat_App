#importing the modules
import socket
import threading


HOST = '127.0.0.1'
PORT = 1234 #port can be any number between 0-65535

def main():
    #AF_INET means we are using IPv4 Addresses
    #SOCK_STREAM means TCP type of communication is carried
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #creating a atry catch block
    try:
        server.bind((HOST, PORT))
        print(f"Running the server on host {HOST} and port {PORT}")
    except:
        print(f"unable to bind to host {HOST} and port {PORT}")  #checks if the HOST and PORT addresses are connected(binded) or not.
    #server.listen(5)


    #this while loop will keep listening to the client connections

    while 1:
        client, address = server.accept()
        print(f"succesfully connected to {address[0]},{address[1]}")
    

     
    
if __name__=="__main__":
    main()
