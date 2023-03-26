from collections import deque
import sys

sys.setrecursionlimit(100000)

test_case=int(input())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def func(x,y):
    grid[y][x]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx<0 or nx>=row or ny<0 or ny>=col:
            continue

        if grid[ny][nx]==1:
            func(nx,ny)
            
    
for _ in range(test_case):
    cnt=0
    row,col,j=map(int,input().split())
    grid=[[0] * row for _ in range(col)]
    
    for _ in range(j):
        x,y=map(int,input().split())
        grid[y][x]=1
    
    for yy in range(col):
        for xx in range(row):
            if grid[yy][xx]==1:
                func(xx,yy)
                cnt+=1
    
    print(cnt)
