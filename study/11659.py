import sys
input=sys.stdin.readline

tmp=[1,3,5,11]

def ttmp(n):
    
    if n==1:
        print(1)
    elif n>4:
        for i in range(5,n+1):
            tmp.append(((tmp[i-3]*2)+tmp[i-2])%10007)
        print(tmp[n-1])
            
    else: 
        print(tmp[n-1])
        

n=int(input().rstrip())

ttmp(n)
