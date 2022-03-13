import matplotlib.pyplot as plt
import seaborn as sns
import random
import pandas as pd
import seaborn as sns
import numpy as np

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



# x=np.linspace(-np.pi, np.pi, 100)
# plt.plot(x,np.sin(x))
# plt.plot(x,np.cos(x))
# plt.show()


# a=np.arange(-5,5)
# print(a[a<0])
# mask1 = abs(a) > 3
# mask2 = a%2==0
# print(a[mask1+mask2])
