n,k=map(int,input().split())

lst=[i+1 for i in range(n)]
result=[]

while True:
    if len(lst)==0:
        break
    
    for i in range(3):
        if i<2:
            lst.append(lst.pop(0))
        else:
            result.append(lst.pop(0))

print("<",end="")     
for i in range(len(result)):
    if i!=len(result)-1:
        print(str(result[i])+", ",end="")
    else:
        print(str(result[i])+"",end="")
print(">",end="")
