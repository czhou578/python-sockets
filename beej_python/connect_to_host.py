import socket

host = "127.0.0.1"
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.create_connection((host, port))

sock.listen(5)