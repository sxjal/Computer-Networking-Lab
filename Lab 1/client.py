
import socket			 
 
s = socket.socket()		 

 
port = 3005			
ip = '192.168.0.201'

try:  
    print("trying",ip)
    s.connect((ip, port)) 
    print("connected")
except:
    print('error')

print (s.send('Thankssomuch for conencting'.encode()))
 
s.close()	 
	
