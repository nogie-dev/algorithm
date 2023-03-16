n,m=map(int,input().split())
grid=[[0]*m for _ in range(n)]
block=input().split()

for i in range(m):
    for j in range(int(block[i])):
        grid[(n-1)-j][i]=1

cnt=0

for i in range(n):
    flag=False
    tmp_cnt=0
            
    for j in range(m):
        
        if flag:
            if grid[i][j]==0:
                tmp_cnt+=1
            #다음 벽을 만난 경우
            else:
                cnt+=tmp_cnt
                tmp_cnt=0
        else:
            if grid[i][j]==1:
                flag=True
            
print(cnt)
        
