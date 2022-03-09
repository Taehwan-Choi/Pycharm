import csv
import matplotlib.pyplot as plt
import pandas as pd

plt.rc('font', family = 'Malgun Gothic')
# 한글 폰트가 깨지지 않기 위해서는 필수!!
plt.rcParams['axes.unicode_minus'] = False
# 마이너스 표시가 깨지지 않기 위해서는 필수!!


# f=open('Seoul temperature.csv', 'r', encoding='cp949')
f=open('Seoul temperature.csv')

data=csv.reader(f)
print(data)

header = next(data)
# print(header)

max_temp=-100
max_data=''
result=[]
high = []
low = []
aug_high=[]
jan_high=[]
month=[[],[],[],[],[],[],[],[],[],[],[],[]]
## month = [[]]* 12 를 하면 오류난다. 안에 있는 []의 고유아이디가 12번 "복사"되서 들어간다. 전부 id가 같다.

aug_day=[]
for k in range(31):
    aug_day.append([])
    #총 31번 append를 하는데, 매번 다른 id의 빈 리스트가 들어간다. 복사되는 것이 아니므로 주의!!!


for row in data:
    try :
        row[-1] = float(row[-1])
        row[-2] = float(row[-2])

        month[int(row[0].split('-')[1])-1].append(row[-1])

        if row[0].split('-')[1] == '08':
            aug_day[int(row[0].split('-')[2])-1].append(row[-1])

        if row[0].split('-')[1] == '08':
            aug_high.append(row[-1])
        if row[0].split('-')[1] == '01':
            jan_high.append(row[-1])

        if row[0].split('-')[0] > '1983' and row[0].split('-')[1] == '02' and row[0].split('-')[2] == '14' :
            result.append(row[-1])
            high.append(row[-1])
            low.append(row[-2])

        if row[-1] > max_temp:
            max_temp = row[-1]
            max_data = row[0]
        # print(row)
    except :
        pass

# print(max_temp)
# print(max_data)




f.close()


# plt.figure(figsize=(10,2))
# # plt.plot(result,'r--')
# plt.plot(high,'r')
# plt.plot(low)
# plt.title("최대 최저기온 비교")
# print(len(result))

#
# plt.plot([1,2,3,4],[10,14,8,3],label='skyblue',color='skyblue', linestyle='--')
#
# plt.plot([1,2,3,4],[9,3,1,4], ls=':', label='dotted')
#
# plt.plot([1,2,3,4],[3,4,1,2], 'r^--')     # .는 점찍기 / ^는 삼각형
# plt.legend()  # 범례표시
#
# plt.title("타이틀이다.")




# plt.hist(aug_high,bins=100, color='r',label='Aug')
# plt.hist(jan_high,bins=100, color='b',label="Jan")

# plt.boxplot([aug_high, jan_high], labels=["Aug","Jan"])


# plt.boxplot(month)


# plt.boxplot(aug_day,showfliers=False)
#fliers는 이상치로 아웃라이어를 숨겨준다.

# plt.legend()
#bins 는 히스토그램의 가로축의 분할 개수를 의미한다 (Bin = 막대)

#
# f=open('Age.csv')
# data=csv.reader(f)
# head=next(data)
#
# print(head)
#
# dongne=str(input("어느 동네의 인구 분포를 확인하시겠습니까? : "))
#
# sindorim=[]
#
# for row in data:
#     if dongne in row[0]  :
#         for k in range(3,14):
#             sindorim.append(row[k])
#
# new=[]
#
# for k in sindorim:
#     new.append(int(k.replace(",","")))
#
# # plt.plot([0,10,20,30,40,50,60,70,80,90,100],new, color = 'r')
# plt.bar([0,10,20,30,40,50,60,70,80,90,100],new, color = 'r')
# # plt.barh(range(5,110,10),new, color = 'r')   # bar 차트인데 horizontally
# plt.title(f"{dongne}의 인구분포")
# plt.style.use("ggplot")
#
# f.close()




f=open("Gender.csv")
data=csv.reader(f)

head=next(data)
print(head)

male=[]
female=[]

# dongne=input("어느 동네 인구를 찾아보시겠습니까? : ")
# dongne="신도림"
dongne="제주특별자치도"



for row in data:
    if dongne in row[0]:
        for k in range(3,24):
            male.append(row[k])
        for k in range(26,47):
            female.append(row[k])
        break
        #굳이 break를 쓰는 경우는, 여러개가 검색되는 경우를 막기위해서

for k in range(21):
    male[k]=int(male[k].replace(",",""))
    female[k]=-int(female[k].replace(",",""))

plt.style.use("ggplot")
# plt.barh(range(0,101,5),male,color='b',label="Male")
# plt.barh(range(0,101,5),female,color='r',label="Female")
# plt.title(f"{dongne}의 남/여 인구 분포")
# plt.legend()
# plt.show()

#
# plt.title(f"{dongne}의 성별 분포 파이 그래프")
# plt.pie([sum(male),-sum(female)],labels=["남성","여성"],startangle=90, autopct="%.1f%%",colors=['b','r'])
# plt.show()


#
# ##혈액형 파이차트를 멋지게 표현하기
# size=[2441,2312,1031,1233]
# label=['A형', 'B형', 'AB형', 'O형']
# plt.axis('equal')
# plt.pie(size,labels=label,autopct="%.1f%%",explode=(0,0,0.2,0),startangle=90)
# #autopct는 auto percent로 뒤 양식대로 표시해주고, explode는 튀어나오는 정도를 의미
# plt.legend()
# plt.show()


#성별분포 꺽은선 그래프
for k in range(len(female)):
    female[k]=-female[k]

# plt.title(f"{dongne}의 성별 분포 꺽은선 그래프")
# plt.plot(range(0,101,5),male,color='b',label="남성")
# plt.plot(range(0,101,5),female,color='r',label="여성")
# plt.legend()
# plt.show()


#남성 - 여성 의 연령별 차이
# diff=[]
# for k in range(21):
#     diff.append(male[k]-female[k])
# plt.title("연령별 남성-여성의 차이")
# plt.bar(range(0,101,5),diff)
# plt.show()



#연령별 남여 인구를 산점도로 표현

plt.title("연령별 남성, 여성 산점도")
import math
size=[]
for k in range(21):
    size.append(math.sqrt(male[k])+math.sqrt(female[k]))
plt.scatter(male,female, s=size, c=range(21),alpha=0.5,cmap='ocean')
plt.xlabel('남성 인구')
plt.ylabel('여성 인구')
#scatter는 단순히 관계를 그리기만 하고, 버블의 크기는 size인 s로 지정한다. color도 크기에 연동하기 위해 같이 지정한다.
#cmap은 컬러맵으로 취향에 따라 선택하면 된다.
#alpha값을 주면 투명하게 만든다.(점이 겹치는 것을 막기 위해서), 0에 가까울 수록 투명해진다.
plt.colorbar()
plt.plot(range(max(male)),range(max(male)),'g')
# 위 코드는 추세선을 추가하는 것
plt.show()