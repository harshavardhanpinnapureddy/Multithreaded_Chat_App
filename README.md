# Multithreaded_Chat_App
This project gives the idea of how multithreaded client-server models work in real time.
It is developed in python using socket programming and TCP is the connection oriented protocol used for this project.

Multithreading concept is used to listen for the messages sent from the already connected client and to listen if any new clients are requesting for the server to connect, concurrently.

# How to run the application
1. verify whether python 3.8 is installed in the computer in hand.
2. change the directory to the project directory.
3. run the server file first.(if client file is ran first it cannot get connected to the server file).
4. python3 server.py  (command for sever file)
5. run the client file for 2 different clients, enter user name and start the conversation.
6. python3 client.py    (command to execute client file)

# Concepts and working scheme
There are two sides of this project, the server side and the client side. The server has two duties one is to listen if any client is sending request to connect to the server and the other task is to listen to each of the connected clients if they have sent any new message. This is carried out using the concept of multithreading, one thread creates new threads for each of the new clients and these internal threads of each of these clients are responsible for checking the messages sent by the server.

Apart from the server side there is client side which has a socket to connect ot the server.

Mutex is used to prevent multiple users entering the shared resource(active clients list) at a time.

# Internal Working
1. After executing the server file and client file, the server end shows the ip and port number of clients connected.
2. On the client side, it asks for the user to enter username, which is displayed to all the other users and in the server clients list.
3. Information related to entry and exit of the clients are displayed on the server side.
4. Inorder to avoid discripancies at the time of termination, "exit", a special message is declared which kills the client thread and terminates the execution. and this exit info is displayed on the server side.

# Extra features added
1. Notifying the usernames at the time of entry and exit on the server end.
2. Setting a limit of 5 clients in the network.
3. giving error messages like "Username can't be empty" on the command line(if any).
4. Notifying the client whenever a new message is recieved.
5. declaring a special message for the termination of the client program for the sake of smooth running of the server client model, since the threads that were not killed would cretae a trouble.


# learning 
Got to know about socket programming, client server model and understood the uses of OS concepts like multi threading and mutex in real life.
