# import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import random
import csv

plt.rc('font', family = 'Malgun Gothic')
# 한글 폰트가 깨지지 않기 위해서는 필수!!
plt.rcParams['axes.unicode_minus'] = False
# 마이너스 표시가 깨지지 않기 위해서는 필수!!


# f=open("SubwayFee.csv")
# data=csv.reader(f)
# header=next(data)
#
# print(header)

# for row in data:
#     for k in range(4,8):
#         row[k]=int(row[k])
#     print(row)


#### 유임승차 비율이 가장 높은 곳
# max=0
# rate=0
# for row in data:
#     for k in range(4,8):
#         row[k]=int(row[k])
#     if row[6]==0:
#         continue
#     else :
#         rate = row[4]/row[6]
#         if rate > max:
#             max=rate
#             print(row, f'max값은 {round(max,2)}')
# print(max)




################유무임 합쳐서 구하기
#
# max=0
# rate=0
# finalword=''
# for row in data:
#     for k in range(4,8):
#         row[k]=int(row[k])
#     if row[6]==0 or row[4]+row[6] <= 100000:
#         continue
#     else :
#         rate = row[4]/(row[4]+row[6])
#         if rate > max:
#             max=rate
#             finalword=row[3] + row[1] + '  :  ' + str(round(max*100,2))
#         if rate > 0.94:
#             print(row, f'max값은 {round(max,2)}')
#
# print(finalword)



################각 항목 가장 많은 숫자 구하기

#
# many=[0]*4
# station=['']*4
# label=['유임승차', '유임하차', '무임승차', '무임하차']
#
# for row in data:
#     for k in range(4,8):
#         row[k]=int(row[k])
#     for i in range(4):
#         if row[4+i] > many[i]:
#             many[i]=row[4+i]
#             station[i]=row[3]+ row[1]
#
# for i in range(4):
#     print(label[i] +' :  ' +  station[i]+'  ' + str(many[i]))

############# 파이차트 자동 생성 + 이미지로 저장
#
# label=['유임승차', '유임하차', '무임승차', '무임하차']
# for row in data:
#     for k in range(4,8):
#         row[k]=int(row[k])
#     plt.figure(dpi=300)
#     plt.title(row[3]+ ' ' + row[1])
#
#     plt.pie(row[4:8], autopct='%1.f%%', labels=label)
#
#     plt.savefig(row[3]+ ' ' + row[1] + '.png')
#     plt.show()



#######################


f=open("SubwayTime.csv")
data=csv.reader(f)

header=next(data)

print(header)

print(next(data))
#
# max=0
# station=''
#
# result=[]
# for row in data:
#     row[4:]=map(int,row[4:])
#     ####map은 1인수의 함수를 2인수의 리스트에 개별적으로 전부 적용한단 뜻
#     # result.append(row[10])
#     # temp=sum([row[10],row[12],row[14]])  ## 7~9시 승차
#     temp = sum([row[11], row[13], row[15]])
#
#     result.append(temp)
#     if temp > max:
#         max=temp
#         station=row[1] + ' ' + row[3]



#
# result.sort()
# plt.bar(range(len(result)),result)

# print(station, max)



###########해당 시간대에 가장 많이 타는 역

hour=23    ## 2h-4가 승차 인덱스

max=0
station=''

daymax=[0]*24
daystation=['']*24

sumin=[0]*24
sumout=[0]*24

result=[]
for row in data:
    row[4:]=map(int,row[4:])


    temp=row[2*hour-4]
    if temp > max:
        max=temp
        station=row[1] + ' ' + row[3]

    for k in range(24):
        sumin[k] += row[2*k+4]
        sumout[k] += row[2*k +5]


        a=k*2+4
        # a=k*2+5 하면 시간대별 하차가 많은 역을 보여준다
        if row[a]>daymax[k]:
            daymax[k] = row[a]
            daystation[k] = row[1] + row[3] + f'({(k+4)%24})'

print(daystation)
print(daymax)


# print(station, max)

# plt.bar(range(24),daymax)
# plt.xticks(range(24),labels=daystation, rotation=90)
# plt.show()


plt.title("지하철 시간대별 승하차 인원 추이")
plt.plot(sumin, label='승차')
plt.plot(sumout, label='하차')
plt.legend()
plt.xticks(range(24),range(4,28))
plt.show()

