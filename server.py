import socket

# Create a socket object
s = socket.socket()

# Bind the socket to localhost and port 8000
s.bind(('localhost', 8000))

# Listen for client connections
s.listen(5)
print("Server is waiting for a connection...")

# Accept a connection from the client
c, addr = s.accept()
print(f"Connected with client: {addr}")

# Communication loop
while True:
    # Receive data from client
    ClientMessage = c.recv(1024).decode()
    print("Client >", ClientMessage)

    # Exit condition (if client sent 'exit')
    if ClientMessage.lower() == 'exit':
        print("Client disconnected. Closing connection.")
        break

    # Send response from server
    msg = input("Server > ")
    c.send(msg.encode())

    # Server side exit
    if msg.lower() == 'exit':
        print("Server disconnected.")
        break

# Close the connection
c.close()