dig=[]
for i in range(9):
    dig.append(int(input()))
dig.sort()
target=sum(dig)-100

test=[]
result=[]

for i in dig:
    for j in dig:
        if i==j:
            continue
        elif i+j==target:
            test.append(i)
            test.append(j)
            break
    if len(test)==2:
        break

test=list(set(test))
for i in dig:
    if i!=test[0] and i!=test[1]:
        result.append(i)

for i in result:
    print(i)
