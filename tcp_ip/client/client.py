import socket
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
machine=socket.gethostbyname(socket.gethostname())
port=9999


c.connect((machine,port))

while True:
    f=input("Enter file name to recieve:")
    c.send(f.encode())
    data=c.recv(1024)
    if(data):
        print("Creating file and saving")
        with open("recv.txt","wb") as f:
            f.write(data)
            print("Data recv")
            break
    else:
        print("Error occured")
        break
