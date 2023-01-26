import math
import random

def find_coprime(phi):
    while True:
        e=random.randrange(2,phi)
        if(math.gcd(e,phi)==1):
            return e

def find_private_key(e, phi):
    d = 0
    k = 1
    while True:
        d = (phi * k + 1) / e
        if d.is_integer():
            return int(d)
        k += 1

def enc(text,e,n):
    cipher=[]
    for symbol in text:
        temp=pow(ord(symbol),e)
        c=temp%n
        cipher.append(c)
    return (cipher)

def dec(text,d,n):
    plain=[]
    for symbol in text:
        temp=pow(symbol,d)
        res=temp%n
        plain.append(chr(res))
    return "".join(plain)


p=int(input("Enter p:"))
q=int(input("Enter q:"))
n=p*q
phi=(p-1)*(q-1)
e=find_coprime(phi)
d=find_private_key(e,phi)
plaintext = input("Enter Plaintext: ")
ciphertext = enc(plaintext, e, n)

print(f'Plaintext: {plaintext}')
print(f'Ciphertext: {ciphertext}')
print(f'Decrypted message: {dec(ciphertext, d, n)}')


