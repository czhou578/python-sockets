import socket

host = input("Enter host name: ")

results = socket.getaddrinfo(host, None)

for result in results:
    family, sockType, proto, cannonName, sockaddr = result
    ipAddr = sockaddr[0]

    print(f"IP address: {ipAddr}")