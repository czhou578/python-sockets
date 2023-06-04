import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6060))

s.listen(5)

while True:
    clientSocket, address = s.accept()
    print(f"connection established for {address}")
    clientSocket.send(bytes("welcome to server", "utf-8"))
    