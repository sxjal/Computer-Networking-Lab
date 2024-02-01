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
        print(chunk)
        if  chunk == "b'break'":
            break
        chunks.append(chunk.decode())
    # Concatenate the chunks to form the complete message
    message = ''.join(chunks)
    return message

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 10000)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('Waiting for a connection...')
    connection, client_address = sock.accept()
    try:
        print('Connection from', client_address)

        # Receive the data in chunks and concatenate them
        data = receive_message(connection)
        print('Received {!r}'.format(data))

        # Send the data back to the client
        send_message(connection, data)
        print('Sent {!r}'.format(data))

    finally:
        # Clean up the connection
        connection.close()
