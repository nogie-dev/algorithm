n=input()

lst=[]

for _ in range(int(n)):
    lst.append(tuple(input("").split(" ")))

tmp=sorted(lst,key=lambda x:int(x[0]))

for a,n in tmp:
    print(a,n)
