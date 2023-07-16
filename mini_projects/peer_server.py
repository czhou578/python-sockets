import socket
import threading

class Peer_Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.peers = []
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def start(self):
        self.socket.bind((self.port, self.host))
        self.socket.listen(5)

        while True:
            client_sock, client_addr = self.socket.accept()

            self.peers.append(client_sock)
            threading.Thread(target=self.handleConnection, args=(client_sock,)).start()
    
    def handleConnection(self, client_sock):

        client_sock.close()