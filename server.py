import socket 

s= socket.socket()

port = 8008
host = '127.0.0.1'

s.bind((host,port))

s.listen(5)

print("socket is listening")

while True:
    c,addr = s.accept()

    print(addr)

    # data = c.recv(1024)

    # print(data)

    # b = bytes("Hi lksdjf","utf-8")

    # c.send(b)


    ### file transfer

    f = open("text.txt","rb")

    l = f.read(1024)

    while (l) :

        c.send(l)

        print('Sent ',l)

        l = f.read(1024)

    f.close()

    c.close()