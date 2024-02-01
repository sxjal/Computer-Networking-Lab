import socket

def send_message(sock, message):
    # Split the message into chunks of 1024 bytes
    chunks = [message[i:i+1024] for i in range(0, len(message), 1024)]
    # Send each chunk separately
    for chunk in chunks:
        sock.send(chunk.encode())

def receive_message(sock):
    # Receive the message in chunks of 1024 bytes
    chunks = []
    while True:
        chunk = sock.recv(1024)
        if not chunk:
            break
        chunks.append(chunk.decode())
    # Concatenate the chunks to form the complete message
    message = ''.join(chunks)
    return message

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
sock.connect(server_address)

# Send a message to the server
while True:
    message = input()
    send_message(sock, message)

    if message == "break":
        break
    
# Receive the response from the server
response = receive_message(sock)
print('Received {!r}'.format(response))

# Clean up the connection
sock.close()
