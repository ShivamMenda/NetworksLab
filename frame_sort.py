import random
class Frame:
    def __init__(self,seqno,data=None):
        self.seqno=seqno
        self.data=data

n=int(input("enter number"))

seqlist=[]
for _ in range(n):
    r=random.randint(1,n*100)
    seqlist.append(r)
print(seqlist)

frames=[]
for _ in range(n):
    ch = random.choice(seqlist)
    frames.append(Frame(ch))
    seqlist.remove(ch)

for i in range(n):
    frames[i].data = input(f"Enter frame data for sequence number {frames[i].seqno}:  ")

frames.sort(key=lambda x:x.seqno)

print("\n---SORTED FRAMES----")
for frame in frames:
    print(f"{frame.seqno} - {frame.data}")
print()