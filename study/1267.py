fee_cnt=int(input())
fee_time_list=input().split()
y_fee_list=[]
m_fee_list=[]

y_standard_fee=10
y_standard_time=30

m_standard_fee=15
m_standard_time=60

for fee_time in fee_time_list:
    if int(fee_time)<=29:
        y_fee_list.append(10)
    elif int(fee_time)>=30 and int(fee_time)<=59:
        y_fee_list.append(20)
    else:
        tmp=(int(fee_time)+y_standard_time)//y_standard_time*y_standard_fee
        y_fee_list.append(tmp)
        
    if int(fee_time)<=59:
        m_fee_list.append(15)
    elif int(fee_time)>=60 and int(fee_time)<=119:
        m_fee_list.append(30)
    else:
        tmp=(int(fee_time)+m_standard_time)//m_standard_time*m_standard_fee
        m_fee_list.append(tmp)
    
if sum(y_fee_list)>sum(m_fee_list):
    print("M",sum(m_fee_list))
elif sum(y_fee_list)<sum(m_fee_list):
    print("Y",sum(y_fee_list))
else:
    print("Y M",sum(m_fee_list))
