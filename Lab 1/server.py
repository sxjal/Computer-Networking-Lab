import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 3005

s.bind(("",port))

s.listen(2)

print('listening at port: ',port)

c,addr = s.accept()
print("connection established with ",addr)

while True:
    clientMsg = c.recv(1024).decode('UTF-8')
    print('Message from Client: ',  clientMsg)   
    if clientMsg == "Terminating connection":
        print("Connection termniated by Server")
        break  
    
    serverMsg = input("Enter Msg: ")
    if serverMsg == 'exit':
        c.send("Terminating connection".encode('UTF-8'))
        break
    c.send(serverMsg.encode('UTF-8'))
    print("Message sent")

s.close()
   
    
   