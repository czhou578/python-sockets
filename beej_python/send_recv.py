import socket

host = '127.0.0.1'
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(sock.getpeername())
# print(socket.gethostname())


sock.connect((host, port))

message = "hello server!"
# sock.send(message.encode())
data = sock.sendto(message.encode(), (host, port))

# data = sock.recv(1024)
data = sock.recvfrom(1024)
received_msg = data.decode()
# received_msg = data.decode()

print(received_msg)

sock.close()

