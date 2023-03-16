import math

def returnTime(time):
    h, m = time.split(':')
    tmp=int(h) * 60 + int(m)
    
    return tmp

def getCarnum(records):
    car_num=[]
    for i in range(len(records)):
        records[i]=records[i].split()
        car_num.append(records[i][1])
    
    car_num=list(set(car_num))
    car_num.sort()
    
    return car_num
    
def getFinalTime(car_records):
    car_io_interval={}
    
    for car_num in car_records:
        tmp_out=0
        tmp_in=0
        
        if len(car_records[car_num])%2==1:
            car_records[car_num].append(['23:59',"OUT"])
            
        for car_io_time in range(len(car_records[car_num])):

            if car_records[car_num][car_io_time][1]=="OUT":
                tmp_out+=returnTime(car_records[car_num][car_io_time][0])
            else:
                tmp_in+=returnTime(car_records[car_num][car_io_time][0])
                
        car_io_interval[car_num]=tmp_out-tmp_in

    return car_io_interval
    

def solution(fees, records):
    car_records={}
    car_final_fee={}
    
    standard_time=fees[0]
    standard_fee=fees[1]
    over_time=fees[2]
    over_fee=fees[3]
    
    car_num=getCarnum(records) #차 번호 뽑아냄
    
    ######차 번호 별로 기록 List#########
    for car_num in car_num:
        tmp_list=[]
        for col in records:
            if car_num in col:
                tmp_list.append([col[0],col[2]])
        car_records[car_num]=tmp_list
    
    #####차 번호 별로 시간 계산###########
    car_io_interval=getFinalTime(car_records)
    for car_num in car_io_interval:
        if car_io_interval[car_num]<=standard_time:
            car_final_fee[car_num]=standard_fee
        else:
            car_final_fee[car_num]=math.ceil((car_io_interval[car_num]-standard_time)/over_time)*over_fee+standard_fee
    
    answer = []
    
    for car_num in car_final_fee:
        answer.append(car_final_fee[car_num])
        
    return answer
    
