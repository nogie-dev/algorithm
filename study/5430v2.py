from collections import deque

ir=[]
buf=deque()
check_buf_len=deque()
result=[]

test_case=int(input())
for i in range(test_case):
    ir.append(input())
    check_buf_len.append(int(input()))
    
    tmp=input().replace('[',"").replace("]","")
    if len(tmp)==0:
        buf.append(deque(""))
    else:
        buf.append(deque(list(map(int,tmp.split(",")))))
    
for lst in range(len(buf)):
    ir_tmp=ir[lst]
    buf_tmp=buf.popleft()
    err_flag=False
    reverse_flag=False
    
    if check_buf_len[lst]!=len(buf_tmp):
        err_flag=True
    
    for i in range(len(ir_tmp)):
        if ir_tmp[i]=="R":
            reverse_flag=reverse_flag^True
            
        if ir_tmp[i]=="D" and len(buf_tmp)!=0:
            
            if reverse_flag:
                buf_tmp.pop()
            else:
                buf_tmp.popleft()
                
        elif ir_tmp[i]=="D" and len(buf_tmp)==0:
            err_flag=True
            break
    
    if reverse_flag:
        buf_tmp.reverse()
        
    if err_flag:
        result.append("error")
    else:
        result.append(list(buf_tmp))
    
    print(result[lst])
    
