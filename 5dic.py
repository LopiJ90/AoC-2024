# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:21:48 2024

@author: lopif
"""

import os

os.chdir(r'C:\Users\lopif\OneDrive\Documenti\AoC')
import pandas as pd
import copy
with open('05b.csv', 'r') as file:
    data = file.read()
    
lists=data.split('\n')

for i in range(len(lists)):
    lists[i]=[int(i) for i in lists[i].split(',')]

order=pd.read_csv('05a.csv',names=['A','B'],sep='|')

#%%

followdict={}

for n in order.A.unique():
    followdict[n]=list(order['B'][order['A']==n])
    

correct=[]
wrong=[]
for i in range(len(lists)):
    corr=1
    for j in range(1,len(lists[i])):
        try:
            err=[k for k in lists[i][:j] if k in followdict[lists[i][j]]]
            print(lists[i][:j],followdict[lists[i][j]] )
        except:
            pass
        if len(err)>0:
            corr=0
            break
    if corr:
        correct.append(i)
    else:
        wrong.append(i)
#%%

final=[lists[i] for i in correct]

tot=0

for lis in final:
    tot=tot+lis[round((len(lis)-1)/2)]

#%%

to_order=[lists[i] for i in wrong]
corrected=[]
for lis in to_order:
    
    conditions=order[order.A.isin(lis) * order.B.isin(lis)]
    cond_or=copy.deepcopy(conditions)
    ordered=[]
    while len(conditions)>0:
        ordered.extend([i for i in conditions.A.unique() if i not in conditions.B.unique()])
        
        conditions=conditions[conditions.A.isin(ordered)==False]
    ordered.extend([i for i in cond_or.B.unique() if i not in cond_or.A.unique()])

    print(len(ordered)==len(lis))
    corrected.append(ordered)
#%%

#corrected=[[i for i in ordered if i in lista] for lista in [lists[i] for i in wrong]]


tot2=0

for lis in corrected:
    tot2=tot2+lis[round((len(lis)-1)/2)]
