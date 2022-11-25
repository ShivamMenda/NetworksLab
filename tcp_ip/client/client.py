import socket
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
machine=socket.gethostbyname(socket.gethostname())
port=9999


c.connect((machine,port))

while True:
    f=input("Enter file name to recv")
    c.send(f.encode())
    try:
        data=c.recv(1024)
        print("Creating file and saving")
        with open("recv.txt","wb") as f:
            f.write(data)
            print("Data recv")
            break
    except:
        print("Error occured")
        break
