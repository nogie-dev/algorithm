import sys
input=sys.stdin.readline

stack=[]

n=input().rstrip()
instruction=[]
for _ in range(int(n)):
    instruction.append(input().rstrip().split(" "))

for i in range(len(instruction)):
    if len(instruction[i]) > 1:
        stack.append(instruction[i][1])
    else:
        if instruction[i][0]=="top":
            if len(stack)==0:
                print("-1")
            else:
                print(stack[len(stack)-1])
        elif instruction[i][0]=="size":
            print(len(stack))
        elif instruction[i][0]=="empty":
            if len(stack)==0:
                print("1")
            else:
                print("0")
        elif instruction[i][0]=="pop":
            if len(stack)==0:
                print("-1")
            else:
                print(stack.pop())
    
    

#print(instruction)
    

