import socket
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
machine=socket.gethostbyname(socket.gethostname())
port=9999


c.connect((machine,port))

while True:
    print("Recieving the file from server")
    data=c.recv(1024)
    fle=str(input("Enter file name to write to:"))
    try:
        print("Creating file and saving")
        with open(f"{fle}.txt","wb") as f:
            f.write(data)
            print("Data recv")
            break
    except:
        print("Error occured")
