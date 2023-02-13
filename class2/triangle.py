import sys

while True:
    lst=[]
    a,b,c=map(int,input().split())
    
    if a==0 and b==0 and c==0:
        break
    
    lst.append(a)
    lst.append(b)
    lst.append(c)
    
    lst.sort()
    
    if pow(lst[2],2)==pow(lst[0],2)+pow(lst[1],2):
        print("right")
    else:
        print("wrong")
