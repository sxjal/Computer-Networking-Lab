import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 3005

localhost = '192.168.0.178'
s.bind(("",port))

s.listen(0)
 


c,addr = s.accept()
while True:
    print('message',  {c.recv(1024).decode('UTF-8')} )    
    print('enter msg')
    sendmsg = input()

    c.send(sendmsg.encode('UTF-8'))
    print('sent')



   
    
   