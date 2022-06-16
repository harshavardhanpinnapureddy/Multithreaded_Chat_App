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
