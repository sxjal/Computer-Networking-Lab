import socket
import time
import random
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 3005

localhost = '192.168.0.209'
s.bind(("",port))

s.listen(0)
 
#c,addr = s.accept()
flag = 1
c,addr = s.accept()

msgrec = 0
msgdrp = 0
while True :

    rand = random.random()
    print("random ", rand)
    if  rand > .6:
        print("msg recieved from client")
        print('message',  {c.recv(1024).decode('UTF-8')} )
        c.send("recv".encode('UTF-8'))
        msgrec += 1
    else:
        print("msg dropped")
        print('message',  {c.recv(1024).decode('UTF-8')} )
        c.send("dropped".encode('UTF-8'))
        msgdrp += 1
    print("total ", msgdrp + msgrec)
    print("msgdrop ", msgdrp )
    print("msgrecv ", msgrec )
    
    


 


   
    
	
# import socket

# # take the server name and port name
# host = 'local host'
# port = 5000

# # create a socket at server side
# # using TCP / IP protocol
# s = socket.socket(socket.AF_INET, 
# 				socket.SOCK_STREAM)

# # bind the socket with server
# # and port number
# s.bind(('', port))

# # allow maximum 1 connection to
# # the socket
# s.listen(1)

# # wait till a client accept
# # connection
# c, addr = s.accept()

# # display client address
# print("CONNECTION FROM:", str(addr))

# # send message to the client after 
# # encoding into binary string
# c.send(b"HELLO, How are you ? \
# 	Welcome to Akash hacking World")

# msg = "Bye.............."
# c.send(msg.encode())

# # disconnect the server
# c.close()

# import socket


# def server_program():
#     # get the hostname
#     host = socket.gethostname()
#     port = 5000  # initiate port no above 1024

#     server_socket = socket.socket()  # get instance
#     # look closely. The bind() function takes tuple as argument
#     server_socket.bind((host, port))  # bind host address and port together

#     # configure how many client the server can listen simultaneously
#     server_socket.listen(2)
#     conn, address = server_socket.accept()  # accept new connection
#     print("Connection from: " + str(address))
#     while True:
#         # receive data stream. it won't accept data packet greater than 1024 bytes
#         data = conn.recv(1024).decode()
#         if not data:
#             # if data is not received break
#             break
#         print("from connected user: " + str(data))
#         data = input(' -> ')
#         conn.send(data.encode())  # send data to the client

#     conn.close()  # close the connection


# if __name__ == '__main__':
#     server_program()