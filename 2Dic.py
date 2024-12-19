# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 08:54:44 2024

@author: lopif
"""

import pandas as pd 

data=pd.read_csv(r'C:\Users\lopif\OneDrive\Documenti\AoC\02.csv',sep=' ',names=range(8),engine='python')
#%%

import numpy as np

dataN=np.array(data)

#%%

dataDiff=np.zeros((1000,7))
for i in range(7):
    dataDiff[:,i]=dataN[:,i+1]-dataN[:,i]
#%%

dfd=pd.DataFrame(dataDiff)

ind1=[i for i in range(1000) if max(list(abs(dfd.loc[i,:])))<=3]
ind2=[i for i in ind1 if 0 not in list(dfd.loc[i,:])]
ind3=[i for i in ind2 if pd.Series(np.sign(dfd.loc[i,:])).nunique()==1]

dfdFin=dfd.loc[ind3,:]
#%%

def is_valid(lista):
    val=1
    lista_dif=[]
    for a in range(1,len(lista)):
        lista_dif.append(lista[a]-lista[a-1])
    if max([abs(i) for i in lista_dif])>3:
        val=0
    if 0 in lista_dif:
        val=0
    if pd.Series(np.sign(lista_dif)).nunique()>1:
        val=0
    return val

#%%


sum([is_valid(data.loc[i,:].dropna()) for i in data.index])
#%%

data.loc[0,:].dropna().pop(0)
#%%
numval=0
for l in data.index:
    nums=data.loc[l,:].dropna()
    if is_valid(nums):
        numval+=1
    else:
        for j in range(len(nums)):
            numpop=nums[[k for k in range(len(nums))if k!=j]].reset_index(drop=True)
            if j>0:
                print(j)
            if is_valid(numpop)==1:
                numval+=1
                break