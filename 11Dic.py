# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 17:15:56 2024

@author: lopif
"""

data=
import pandas as pd
import copy
#%%
from tqdm import tqdm
data=[int(i) for i in data.split()]

for i in range(25):
    newdata=[]
    for j in data:
        let=str(j)
        A=round(len(let)/2)
        if j==0:
            newdata.append(1)
        elif len(let)%2==0:
            newdata.extend([int(let[:A]),int(let[A:])])
        else:
            newdata.append(j*2024)
    data=newdata
    print(len(data))
#%%
data=pd.Series([int(i) for i in data.split()])

vals=data.value_counts()

for i in tqdm(range(100)):
    newvals=pd.Series()
    for j in vals.index:
        let=str(j)
        A=round(len(let)/2)
        if j==0:
            if 1 in newvals.index:
                newvals[1]+=vals[0]
            else:
                newvals[1]=vals[0]
        elif len(let)%2==0:
            C=int(let[:A])
            D=int(let[A:])
            if C in newvals.index:
                newvals[C]+=vals[j]
            else:
                newvals[C]=vals[j]
            if D in newvals.index:
                newvals[D]+=vals[j]
            else:
                newvals[D]=vals[j]
        else:
            E=j*2024
            if E in newvals.index:
                newvals[E]+=vals[j]
            else:
                newvals[E]=vals[j]

    vals=copy.deepcopy(newvals)

list(newvals.index)

#%%

ids=newvals.index
ids2=newvals.index
#%%

[i for i in ids if i not in ids2]
