import socket

seq_data = {}
 
def receive_message(sock):
     
    while True:
        serverMsg = s.recv(1024).decode('UTF-8')
        seqno,data = serverMsg.slpit(':')
        print("Data Received ",seqno,":",data)
        seq_data[int(seqno)] = data

    message = ''.join(chunks)
    return message

 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
s.connect(('127.0.0.1', 3005))
print("connected with server")

while True:
    response = receive_message(s)
    print('Received {!r}'.format(response))

# Clean up the connection
s.close()
