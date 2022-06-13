#importing the modules
import socket
import threading


HOST = "127.0.0.1"
PORT = 1234
def main():
    pass
    #creating a socket for the client side
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #connect to the server
    try:
        client.connect((HOST,PORT))
        print("Successfully connected to the server")
    except:
        print(f"Unable to connect to host {HOST} and port {PORT}")


if __name__=="__main__":
    main()