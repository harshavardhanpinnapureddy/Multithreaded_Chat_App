#import the libraries
import socket
import sys
import collections
import time
import threading

from threading import Thread

HOST='127.0.0.1'
PORT=1234
active_clients=[] #this contains the list of clients who are active.
lock=threading.Lock()  #this lock serves as a mutex to enter and exit the critical section(shared client map)

#thread function that listens to the client till the server is connected
def listen_for_messages(client, username):
    #print(f"{username} thread")
    #print("here")
    while 1:
        message=client.recv(2048).decode('utf-8')
        #print(message)
        if message=="exit":
            lock.acquire()
            active_clients.remove((username,client))
            lock.release()
            print(f"{username} has left the server")
            exit(0)
        elif message != '':
            final_message=username+'~'+message
            send_messages_to_all(final_message)

        

#function to send message to only one client
def send_message_to_client(client, message):
    client.sendall(message.encode())

#function to send any new message to all the users
def send_messages_to_all(message):
    lock.acquire()
    for user in active_clients:
        send_message_to_client(user[1], message)
    lock.release()

def print_group_participants():
    lock.acquire()
    for user in active_clients:
        print(user[0])
    lock.release()

#function to handle client
def client_handler(client):
    #server will listen for client message that contains the username.
    while 1:
        username = client.recv(2048).decode('utf-8')
        if username!='':
            lock.acquire()
            active_clients.append((username, client))
            lock.release()
            print(f"{username} dived in")
            break
        else:
            print('Client username is empty')
    threading.Thread(target=listen_for_messages, args=(client, username)).start()

def main():
    #AF_INET means IPV4
    #SOCK_STREAM means TCP
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        server.bind((HOST,PORT))
        print(f"Running the server on {HOST} {PORT}")
    except:
        print(f"Unable to bind to {HOST} and port {PORT}")

    #set server limt
    server.listen(5)

    #this loop is to keep listening to the client.
    while 1:
        client, address = server.accept()
        print(f"Successfully connected to client {address[0]} {address[1]}")
        threading.Thread(target=client_handler, args=(client, )).start()



if __name__ == '__main__':
    main()