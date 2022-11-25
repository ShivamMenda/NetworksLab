class Frame:
    def __init__(self,num,data):
        self.frameNo = num
        self.data = data
    def __str__(self):
        return f"{self.frameNo}{self.data}"

def sort(frames):
     for i in range(len(frames)-1):
        for j in range(len(frames)-1-i):
            if(frames[j].frameNo > frames[j+1].frameNo):
                frames[j],frames[j+1] = frames[j+1],frames[j]

n=int(input("Enter the no of frames: "))
frames=[]
print("Enter frames no and data: ")
for i in range(n):
    nums,data = input().split()
    nums = int(nums)
    frames.append(Frame(nums,data))
print("Frames after sorting: ")
sort(frames)
for i in frames:
    print(i.frameNo, i.data)