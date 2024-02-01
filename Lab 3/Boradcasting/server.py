import socket
import time
import ipaddress

IP = '192.168.0.201'
MASK = '255.255.255.0'

host = ipaddress.IPv4Address(IP)
net = ipaddress.IPv4Network(IP + '/' + MASK, False)
# print('Broadcast:', net.broadcast_address)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

# Enable broadcasting mode
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Set a timeout so the socket does not block
# indefinitely when trying to receive data.
server.settimeout(0.2)
# message = b"your very important message"
while True:
    # message = input("Enter message: ")
    message = "band karo".encode("utf-8")[:1024]
    if message.lower() == "close":
        print("closing...")
        break
    while True:
        server.sendto(message, ('<broadcast>', 37020))
    print("message sent!")
    time.sleep(1)
server.close()
