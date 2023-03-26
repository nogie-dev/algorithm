import sys

input=sys.stdin.readline

n,m=map(int,input().rstrip().split())
num_list=input().rstrip().split()
num_list=list(map(int,num_list))

all_sum=[]
sums=0
for i in num_list:
    sums+=i
    all_sum.append(sums)

for _ in range(m):
    l1,l2=map(int,input().rstrip().split())
    
    if l1-1==0:
        print(all_sum[l2-1])
    else:
        print(all_sum[l2-1]-all_sum[l1-2])
    


