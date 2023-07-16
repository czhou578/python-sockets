import socket
import threading

class Peer:
    def __init__(self, host, port):
        self.port = port
        self.host = host
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    
    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print(f"Listening on port {self.port}")

        while True:
            client_socket, client_address = self.socket.accept()

            threading.Thread(target=self.handleConnection)
    
    def handleConnection(self, client_socket):

        client_socket.close()

    def download_file(peer_ip, peer_port, file_name):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((peer_ip, peer_port))

        sock.sendall(file_name.encode())

        file_content = b""

        while True:
            data = sock.recv(4096)
            if not data:
                break
            file_content += data
        
        with open(file_name, "wb") as file:
            file.write(file_content)
        
        sock.close()
    
    def upload_file(client_socket, file_path):
        with open(file_path, "rb") as file:
            file_content = file.read()

        client_socket.sendall(file_content)
        client_socket.close()


    