import socket

s = socket.socket()

port = 8008
host = '127.0.0.1'

s.connect((host,port))

### sending message

# name = input("Enter your name: ")

# s.send(bytes(name,"utf-8"))

print(s.recv(1024))

s.close()