
import socket			  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 3005

#ip of the server
ip = '10.10.51.190'

try:  
    print("trying ",ip)
    s.connect((ip, port)) 
    print("Connected with ",ip)
except:
    print('error')
    

while True:
    clientMsg = input("Enter Msg: ")
    if clientMsg == 'exit':
        s.send("Terminating connection".encode('UTF-8'))
        break
    s.send(clientMsg.encode('UTF-8'))
    print("Message sent")
    
    serverMsg = s.recv(1024).decode('UTF-8')
    print('Message from Server: ',  serverMsg)
    if serverMsg == "Terminating connection":
        print("Connection termniated by Server")
        break    

s.close()	 
	
