#import the libraries
import socket
import sys
import collections
import time
import threading


from threading import Thread

HOST='127.0.0.1'
PORT=1234
flag=1

#this function listens message continously from the server
def listen_to_server(client,flag):
    while flag:
        message=client.recv(2048).decode('utf-8')
        print("New message recieved")
        if message != '':
            username = message.split('~')[0]
            content = message.split('~')[1]
            print(f"[{username}] {content}")
        

#this function is to send messages from client to the server
def send_message_to_server(client):
    while 1:
        message = input('Message : ')
        if message != '':
            client.sendall(message.encode())
        if message=="exit":
            flag=0
            sys.exit()

def communicate_to_server(client):
    username=input('Enter username : ')
    if username!='':
        client.sendall(username.encode())
    else:
        print('Username cannot be empty')
        exit(0)

    x=threading.Thread(target=listen_to_server, args=(client, flag))
    x.daemon=True
    x.start()
    send_message_to_server(client)



def main():
    #creating a socket object
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #connect to the server
    try:
        client.connect((HOST,PORT))
        print("Successfully connected to server")
    except:
        print(f"Unable to connect to server {HOST} {PORT}")

    communicate_to_server(client)

if __name__=="__main__":
    main()