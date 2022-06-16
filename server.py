#import the libraries
import socket
import threading

HOST='127.0.0.1'
PORT=1234
active_clients=[] #this contains the list of clients who are active.

#thread function that listens to the client till the server is connected
def listen_for_messages(client, username):
    #print(f"{username} thread")
    #print("here")
    while 1:
        message=client.recv(2048).decode('utf-8')
        #print(message)
        if message != '':
            final_message=username+'~'+message
            send_messages_to_all(final_message)
        else:
            print(f'Message sent from client {username} is empty')

#function to send message to only one client
def send_message_to_client(client, message):
    client.sendall(message.encode())

#function to send any new message to all the users
def send_messages_to_all(message):
    for user in active_clients:
        send_message_to_client(user[1], message)

def print_group_participants():
    for user in active_clients:
        print(user[0])

#function to handle client
def client_handler(client):
    #server will listen for client message that contains the username.
    while 1:
        username = client.recv(2048).decode('utf-8')
        if username!='':
            print(f"{username} dived in")
            active_clients.append((username, client))
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