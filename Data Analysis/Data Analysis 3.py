import matplotlib.pyplot as plt
import seaborn as sns
import random
import pandas as pd
import seaborn as sns
import numpy as np
import csv



plt.rc('font', family = 'Malgun Gothic')
# 한글 폰트가 깨지지 않기 위해서는 필수!!
plt.rcParams['axes.unicode_minus'] = False
# 마이너스 표시가 깨지지 않기 위해서는 필수!!


# t=np.arange(0., 5., 0.2)
# plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
# plt.show()


# np.pi
# np.sqrt(2)
# np.sin(0)
# np.cos(np.pi)

# a=np.random.rand(10)
# print(a)
#
# b=np.random.choice(7,10)   #0~6까지 뽑힘
# print(b)
#
# c=np.random.choice(101,40,replace=False)    # 0~100까지만 뽑힘 이렇게 하면, 중복되는 숫자는 뽑히지 않는다.
# print(c)




# dice=np.random.choice(6,10000, p=[0.1,0.2,0.3,0.2,0.1,0.1])
# plt.hist(dice,bins=6)
# plt.show()



# x=np.random.randint(10,100,200)
# y=np.random.randint(10,100,200)
# size=np.random.rand(200)*100
# plt.scatter(x,y,s=size, c=x,alpha=0.7)
# plt.colorbar()
# plt.show()

# a=np.arange(1,2,0.1)
# b=np.linspace(10,15,20)
# print(a)
# print(b)


#
# x=np.linspace(-np.pi, np.pi, 100)
# plt.plot(x,np.sin(x))
# plt.plot(x,np.cos(x))
# plt.show()


# a=np.arange(-5,5)
# print(a[a<0])
# mask1 = abs(a) > 3
# mask2 = a%2==0
# print(a[mask1+mask2])



##################################################### 유사한 인구구조인 행정구역 나타내기

#
# f=open("Age.csv")
# df=pd.read_csv(f, thousands=',')
# df.loc[df['행정구역'].str.contains('신도림동'),'2019년02월_계_0~9세':]

# f=open("Age.csv")
# data=csv.reader(f)
# header=next(data)
# print(header)
# data=list(data)      ####data를 한번만 쓰고 나면 더이상 불러 올 수 없으므로 list 형태로 변환해서 저장하는 것



# label=header[3:]
# town="중계1동"
# home=[]
# nearhome=[]
# neartown=''
# diffsum=10000000000000000000
#
# for row in data:
#     if town in row[0]:
#         for k in row[3:]:
#             temp=int(k.replace(",",''))
#             home.append(temp/int(row[1].replace(",",'')))
#
# for row in data:
#     if town in row[0]:
#         continue
#     templist = []
#     for k in row[3:]:
#         temp1=int(k.replace(",", ''))
#         templist.append(temp1/int(row[1].replace(",",'')))
#     tempsum=0
#     for i in range(11):
#         tempsum+=abs(home[i]-templist[i])
#     if tempsum < diffsum :
#         diffsum = tempsum
#         nearhome = templist
#         neartown=row[0]
#
#
# plt.plot(home,label='신도림동')
# plt.plot(nearhome,label=neartown)
# plt.legend()
# plt.xticks(range(11), labels=label,rotation=90)
# plt.show()
#
#
#

##################################### pandas 다루기

# df=pd.read_html('https://en.wikipedia.org/wiki/List_of_Game_of_the_Year_awards', header=0, index_col=0)
# print(df[4])
##html 주소에서 표 양식으로 된 것은 다 끌어다 준다! df[0], df[1], df[2] 이런식으로 표 여러개를 다 따로 가져옴

#
# index = pd.date_range('1/1/2000',periods=8)
# print(index)
#
# df=pd.DataFrame(np.random.rand(8,3),index=index, columns=['A','B','C'])
# print(df)
#
#
# df[df['A']>0.5]
# df.T
# df['D']=df['A']/df['B']
# df['E']=np.sum(df,axis=1)
#
# ###axis 축은 0,1,2로 되는데, 바깥쪽, 즉 리스트의 껍질부터 0이 된다. 행렬의 경우에는 직선인 리스트가
# ###위로 쌓인 구조이므로, 쌓이는 축인 세로가 0차원 축이라고 할 수 있다. 더 안쪽의 작은 레벨인 가로가 1차원 축이 되는 것
#
# print(df)
# print(df.sub(df['A'],axis=0))
# #세로로 쌓이는 축이 바깥쪽 축이므로 0차원 축이 되고, 그래서 A가 세로로 전부 0이 된다. (전체 칼럼에서 A칼럼을 일괄적으로 뺴준 것)



##############################

df=pd.read_csv("Age.csv", encoding='cp949', index_col=0, thousands=",")
#한글이 깨지지 않기 위해서 encoding='cp949'를 입력하였다

df=df.div(df['2019년02월_계_총인구수'],axis=0)
#세로 방향으로 나눗셈을 일괄 적용한다는 뜻

df=df.drop(['2019년02월_계_총인구수','2019년02월_계_연령구간인구수'],axis=1)
#세로 방향으로 통째로 지우는 거라, axis=0으로 착각! 하기 쉽다. axis=1인 column 에서 앞에 있는 라벨을 찾으란 뜻! 그걸 찾아서 버려라.

name="관악구"

df2=df[df.index.str.contains(name)]    #mask를 이용한 방법이다.

print(df2)


x=df.sub(df2.iloc[0],axis=1)
y=np.power(x,2)
z=y.sum(axis=1)

i=z.sort_values().index[:5]


df.loc[i].T.plot()
# plt.plot(df2.T, label=name)
plt.xticks(range(11),range(0,105,10))
plt.legend()


