import socket

port = 3490
host = '127.0.0.1'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((port, host))

message = "Hello, server!"
sock.sendall(message.encode())

# Receive data from the server
data = sock.recv(1024)
received_message = data.decode()
print("Received:", received_message)

# Close the socket
sock.close()
