
import socket			 
import time

s = socket.socket()		 

 
msgs = ["msg 1","msg 2","msg 3","msg 4","msg 5","msg 7","msg 8","msg 9","msg 10"]
port = 3005			
ip = '192.168.0.209'


print("trying",ip)
s.connect((ip, port)) 
print("connected")
    

for i in range(0,10):
    time.sleep(3)
    trial = 1
    while trial<3:    
        print("sending ",msgs[i])
        s.send(msgs[i].encode('UTF-8'))
        reply = s.recv(1024).decode('UTF-8')
        
        if reply == "dropped" :
            trial += 1
        elif reply == "recv":
            trial = 4
  

s.close()	 
    



# import socket
  
# # take the server name and port name
  
# host = 'local host'
# port = 5000
  
# # create a socket at client side
# # using TCP / IP protocol
# s = socket.socket(socket.AF_INET,
#                   socket.SOCK_STREAM)
  
# # connect it to server and port 
# # number on local computer.
# s.connect(('127.0.0.1', port))
  
# # receive message string from
# # server, at a time 1024 B
# msg = s.recv(1024)
  
# # repeat as long as message
# # string are not empty
# while msg:
#     print('Received:' + msg.decode())
#     msg = s.recv(1024)
 
# # disconnect the client
# s.close()

# import socket


# def client_program():
#     host = socket.gethostname()  # as both code is running on same pc
#     port = 5000  # socket server port number

#     client_socket = socket.socket()  # instantiate
#     client_socket.connect((host, port))  # connect to the server

#     message = input(" -> ")  # take input

#     while message.lower().strip() != 'bye':
#         client_socket.send(message.encode())  # send message
#         data = client_socket.recv(1024).decode()  # receive response

#         print('Received from server: ' + data)  # show in terminal

#         message = input(" -> ")  # again take input

#     client_socket.close()  # close the connection


# if __name__ == '__main__':
#     client_program()