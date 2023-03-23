import sys
from collections import deque

input=sys.stdin.readline

test_case=int(input())
for i in range(test_case):
    ir=input()
    check_buf_len=int(input())
    queue=deque(input().rstrip()[1:-1].split(","))
    reverse_flag=False
    
    if check_buf_len==0:
        queue=[]
    
    for ir in ir:
        
        
        if ir=="R":
            reverse_flag=reverse_flag^True
                
        elif ir=="D":
                
            if len(queue)==0:
                print("error")
                break
            else:
                    
                if reverse_flag:
                    queue.pop()
                else:
                    queue.popleft()

    else:
        if reverse_flag==True:
            queue.reverse()
            print("["+",".join(queue)+"]")
        else:
            print("["+",".join(queue)+"]")
