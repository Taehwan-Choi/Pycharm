import pandas as pd
import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.rc('font',family='malgun gothic')

f='C:/Users/KRA/Desktop/발구지/racedata.csv'

df=pd.read_csv(f, encoding='cp949')
#encoding cp949를 지정!

df.loc[df['포입여부']=='포입말','포입여부']=1
df.loc[df['포입여부'].isna(),'포입여부']=0
df['포입여부']=df['포입여부'].astype(bool)

df.loc[df['심사 합격마']==1.,'심사 합격마']=1
df.loc[df['심사 합격마'].isna(),'심사 합격마']=0
df['심사 합격마']=df['심사 합격마'].astype(bool)


df.loc[df['육성조련사']=='한국생협A','육성조련사']='한국생협'
df.loc[df['육성조련사']=='한국생협B','육성조련사']='한국생협'
df.loc[df['육성조련사']=='한국생협C','육성조련사']='한국생협'

# sns.heatmap(df.corr())