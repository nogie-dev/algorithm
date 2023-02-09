n=input()

lst=[]

for _ in range(int(n)):
    lst.append(tuple(input("").split(" ")))

tmp=sorted(lst,key=lambda x:int(x[0]))

for a,n in tmp:
    print(a,n)

#another ver
n=input()
lst=[]
for _ in range(int(n)):
    lst.append(tuple(input().split(" ")))
lst.sort(key=lambda x:int(x[0]))
for a,n in lst:
    print(a,n)
