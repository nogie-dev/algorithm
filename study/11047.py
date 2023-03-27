import sys

sys.setrecursionlimit(10**7)
input=sys.stdin.readline

n, k = map(int,input().rstrip().split())

cnt=0

def div(tmp_coin):
    global k
    global cnt
    
    if k//tmp_coin!=0:
        tmp=k//tmp_coin
        cnt+=tmp
        k-=tmp*tmp_coin
        
        div(tmp_coin)
        
coin=[]

for _ in range(n):
    coin.append(int(input().rstrip()))

for _ in range(len(coin)):
    tmp_coin=coin.pop()
    
    div(tmp_coin)

print(cnt)


    
