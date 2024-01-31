import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    ip = ""
except socket.gaierror:
    print('error')
    print(socket.gaierror)

print(ip)
port = 80

try:
    s.connect((ip,port))
    print('connected')
except:
    print('something')
print(s)


