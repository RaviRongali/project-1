# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 7000


# connect to the server on local computer
s.connect(("127.0.0.1", port))

# receive data from the server
msg = s.recv(1024)
print(msg.decode("utf-8"))
# close the connection
s.close()
