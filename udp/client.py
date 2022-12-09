import socket

ip=socket.gethostbyname(socket.gethostname())
port=9999
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((ip,port))

print(f"Listening to {ip}:{port}")

while True:
    data,addr=s.recvfrom(1024)
    print(f"Data Received:{str(data.decode())}")
    if(str(data.decode())=="exit"):
        print("Exiting")
        break
    else:
        continue

