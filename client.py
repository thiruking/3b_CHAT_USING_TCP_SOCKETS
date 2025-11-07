import socket

# Create socket
s = socket.socket()

# Connect to the server on localhost with port 8000
s.connect(('localhost', 8000))

# Communication loop
while True:
    msg = input("Client > ")               # Take user input
    s.send(msg.encode())                   # Send message to server

    response = s.recv(1024).decode()       # Receive response from server
    print("Server >", response)