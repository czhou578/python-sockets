import socket

port = 3490

def start_server(port, host):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))

    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()

        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            response = process_data(data)
            client_socket.sendall(response)
    

        client_socket.close()
    
    server_socket.close()

def process_data(data):
    # Process the received data and return a response
    # Example: Echo the received data back to the client
    return data