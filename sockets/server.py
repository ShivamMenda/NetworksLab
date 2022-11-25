#Accept Connections
import socket
s=socket.socket() #Default IPv4 TCP/IP
print("Socket Created")
s.bind(('localhost',9999))

s.listen()
print("Waiting for connections")

while True:
    (c,addr)=s.accept()
    name=c.recv(1024).decode()
    print("Client connected with ",addr,name)
    
    c.send("test message".encode('utf-8'))