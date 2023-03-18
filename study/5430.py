from collections import deque

ir=[]
buf=deque()
check_buf_len=deque()
result=[]

test_case=int(input())
for i in range(test_case):
    ir.append(input())
    check_buf_len.append(int(input()))
    
    buf.append(deque(list(map(int,(input().replace('[',"").replace("]","").split(","))))))

for lst in range(len(buf)):
    ir_tmp=ir[lst]
    buf_tmp=buf.popleft()
    err_flag=False
    
    for i in range(len(ir_tmp)):
        #print("ir:",ir_tmp[i])
        if ir_tmp[i]=="R":
            buf_tmp.reverse()
            #print("this:",buf_tmp)
            
        if ir_tmp[i]=="D" and len(buf_tmp)!=0:
            buf_tmp.popleft()
        elif ir_tmp[i]=="D" and len(buf_tmp)==0:
            err_flag=True
            break
    
    if err_flag:
        result.append("error")
    else:
        result.append(list(buf_tmp))
        
for i in result:
    print(i)
            
        
