import socket
import random

MAX_PACK = 3

def fragment_data(data, max_pack):
    fragments = []
    seq_start = random.randint(100, 999)
    print("seq number: ",seq_start)
    for i in range(0, len(data), max_pack):
        fragment = {
            'sequence_number': seq_start + i,
            'data': data[i:i + max_pack]
        }
        fragments.append(fragment)
    return fragments

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '127.0.0.1'
server_port = 3005

s.bind((server_address, server_port))

while True:
    data = input("Enter the data to be sent: ")
    #seqnumber:data
    fragments = fragment_data(data, MAX_PACK)
    for fragment in fragments:
        seqNO = fragment['sequence_number']
        data1 = fragment['data']
        msg = f'{seqNO}:{data1}'
        s.sendto(msg.encode('utf-8'), (server_address, server_port))

    print(f"Data sent in {len(fragments)} fragments.")
    
    s.sendto("/0".encode('utf-8'),(server_address,server_port))

