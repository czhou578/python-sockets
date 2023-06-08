import socket
import select

host = '127.0.0.1'
port = 3459

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(False)

sock.bind((host, port))

inputs = [sock]

r, w, e = select.select(inputs, [], [])

while True:
    data, client_address = sock.recv(1024)
    message = data.decode()

    response = "response from server"
    sock.sendto(response.encode(), client_address)
