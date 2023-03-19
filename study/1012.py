from collections import deque

test_case=int(input())
#true_cell=[]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
cnt=[]

for _ in range(test_case):
    tmp_list=deque()
    tmp_cnt=0
    row,col,j=map(int,input().split())
    grid=[[0] * row for _ in range(col)]
    
    for _ in range(j):
        x,y=map(int,input().split())
        grid[y][x]=1
        tmp_list.append([x,y])
    
    for _ in range(len(tmp_list)):
        x,y=tmp_list.popleft()
        grid[y][x]=0
        find_flag=False
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or nx>=row-1 or ny<0 or ny>=col-1:
                continue
            else:
                if grid[ny][nx]==1:
                    find_flag=True
        
        if find_flag==False:
            tmp_cnt+=1
            
    cnt.append(tmp_cnt)   

print(cnt)
    
