def solution(fees, records):
    tmp={}
    car_num=[]
    
    for i in range(len(records)):
        records[i]=records[i].split()
        car_num.append(records[i][1])
    
    car_num=list(set(car_num))
    
    for car_num in car_num:
        tmp_list=[]
        for col in records:
            if car_num in col:
                tmp_list.append([col[0],col[2]])
        tmp[car_num]=tmp_list
    
    print(tmp)
    
    answer = []
    return answer