import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
machine=socket.gethostbyname(socket.gethostname())
port=9999

s.bind((machine,port))
s.listen()

print(f"{machine} Waiting for connections")
while True:
    c,addr=s.accept()
    print("Client connected and sending the file to ",addr)
    f=open("test.txt",'rb')
    data=f.read(1024)
    while True:
        if data:
            print("Sending data")
            c.send(data)
            data=f.read(1024)
            print("data sent")
            break
        else:
            print("Failed to send")
            break