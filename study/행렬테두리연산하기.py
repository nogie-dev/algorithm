from collections import deque

def solution(rows, columns, queries):
    grid=[]
    result=[]
    tmp=[]
    for i in range(1,columns*rows+1):
        tmp.append(i)
        if i%columns==0:
            grid.append(tmp)
            tmp=[]
            
    for x_y in queries:
        task_list=deque() 
        x1,y1,x2,y2=x_y
        
        x1-=1
        y1-=1
        x2-=1
        y2-=1
        
        for right in range(y1,y2):
            task_list.append(grid[x1][right])
            
        for to_bottom in range(x1,x2):
            task_list.append(grid[to_bottom][y2])
            
        for left in range(y2,y1,-1):
            task_list.append(grid[x2][left])
            
        for to_top in range(x2,x1,-1):
            task_list.append(grid[to_top][y1])
            
        front=task_list.pop()
        task_list.appendleft(front)
        result.append(min(task_list))
        
        while task_list:
            for right in range(y1,y2):
                grid[x1][right]=task_list.popleft()
                
            for to_bottom in range(x1,x2):
                grid[to_bottom][y2]=task_list.popleft()
                
            for left in range(y2,y1,-1):
                grid[x2][left]=task_list.popleft()
                
            for to_top in range(x2,x1,-1):
                grid[to_top][y1]=task_list.popleft()
            
    return result
