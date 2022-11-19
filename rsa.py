import math
p=int(input("Enter p:"))
q=int(input("Enter q:"))
n=p*q
phi=(p-1)*(q-1)
e=2
while(e<phi):
    if(math.gcd(e,phi)==1):
        break
    else:
        e=e+1

d = 2
while d < phi:
        if ((d*e) % phi)==1:
            break
        else:
            d=d+1


msg=float(input("Enter message in float"))
print("message= ",msg)

c=math.pow(msg,e)
c=math.fmod(c,n)
print("encrypted message= ",c)

res=math.pow(c,d)
m=math.fmod(res,n)
print("Decrypted message= ",m)
