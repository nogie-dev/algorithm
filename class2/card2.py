import sys
from collections import deque
input=sys.stdin.readline
n=input()

lst=deque([i+1 for i in range(int(n))])

while True:
    if len(lst)==1:
        print(lst[0])
        break

    lst.popleft()
    lst.rotate(-1)
