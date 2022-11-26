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
    f1=c.recv(1024).decode()
    try:
            f=open(f"{f1}.txt",'rb')
    except:
            print("File Not found")
            break
    while True:
        
        data=f.read(1024)
        if data:
            print("Sending data")
            c.sendall(data)
            data=f.read(1024)
            print("data sent")
            break
        else:
            print("Failed to send,file does not exist")
            break