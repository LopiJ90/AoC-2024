# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:20:25 2024

@author: lopif
"""
import os

os.chdir(r'C:\Users\lopif\OneDrive\Documenti\AoC')
import pandas as pd

with open('03.txt', 'r') as file:
    data = file.read()
    
mults=data.split('mul(')[1:]

for i in range(len(mults)):
    mults[i]=mults[i].split(')')[0]
    mults[i]=mults[i].split(',')
    if len(mults[i])==1:
        mults[i].append('A')
    
#%%
dataMul=pd.DataFrame(columns=[0,1,2,3])


dataMul[0]=[mults[i][0] for i in range(len(mults))]

dataMul[1]=[text.isnumeric() for text in dataMul[0]]

dataMul[2]=[mults[i][1] for i in range(len(mults))]

dataMul[3]=[text.isnumeric() for text in dataMul[2]]

dataMul=dataMul[dataMul[1]* dataMul[3]>0].astype(int)
#%%

dataMul[4]=dataMul[0]*dataMul[2]

dataMul[4].sum()
#%%

dos=data.split('do()')

for i in range(len(dos)):
    dos[i]=dos[i].split("don't()")[0]
    
dataNew=''.join(dos)

mults=dataNew.split('mul(')[1:]

for i in range(len(mults)):
    mults[i]=mults[i].split(')')[0]
    mults[i]=mults[i].split(',')
    if len(mults[i])==1:
        mults[i].append('A')
    
#%%
dataMul=pd.DataFrame(columns=[0,1,2,3])


dataMul[0]=[mults[i][0] for i in range(len(mults))]

dataMul[1]=[text.isnumeric() for text in dataMul[0]]

dataMul[2]=[mults[i][1] for i in range(len(mults))]

dataMul[3]=[text.isnumeric() for text in dataMul[2]]

dataMul=dataMul[dataMul[1]* dataMul[3]>0].astype(int)

dataMul[4]=dataMul[0]*dataMul[2]

dataMul[4].sum()
