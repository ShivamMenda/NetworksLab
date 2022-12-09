import socket
ip=socket.gethostbyname(socket.gethostname())
port=9999
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print(f"Connected to {ip}:{port}")
while True:
    inp=str(input("Enter message:"))
    msg=bytes(inp,'utf-8')
    print(f"Sending {str(msg.decode())} to {ip}:{port}")
    s.sendto(msg,(ip,port))
    if(inp=="exit"):
        print("Exiting")
        break
    else:
        continue
