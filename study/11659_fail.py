import sys
#from collections import deque

input=sys.stdin.readline

#queue=deque()
#n은 수의 갯수, m은 합을 구해야하는 횟수
n,m=map(int,input().rstrip().split())
num_list=input().rstrip().split()
num_list=list(map(int,num_list))

for _ in range(m):
    l1, l2=map(int,input().rstrip().split())
    print(sum(num_list[l1-1:l2])    


