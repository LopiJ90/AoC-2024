# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:05:51 2024

@author: lopif
"""

import os

os.chdir(r'C:\Users\lopif\OneDrive\Documenti\AoC')
import pandas as pd
from tqdm import tqdm
import numpy as np
with open('08.txt', 'r') as file:
    data = file.read()

lines=lines=[list(i) for i in data.split('\n')]

pos=np.array(lines)
#%%


anti=[]

vals=np.unique(pos)
A=vals.size
for i in range(A):
    sym=str(vals[i])
    print(sym)
    if sym!='.':
        an=np.argwhere(pos==sym)
        B=an.shape[0]
        for j in range(B):
            for k in range(j):
                cd=2*an[j]-an[k]
                print(cd)
                if sum([0,0]<=cd)+sum(cd<pos.shape)==4:
                    anti.append(tuple(cd))
                cd=2*an[k]-an[j]
                print(cd)
                if sum([0,0]<=cd)+sum(cd<pos.shape)==4:
                    anti.append(tuple(cd))
tot=len(set(anti))

#%%

anti=[]

vals=np.unique(pos)
A=vals.size
for i in range(A):
    sym=str(vals[i])
    print(sym)
    if sym!='.':
        an=np.argwhere(pos==sym)
        B=an.shape[0]
        for j in range(B):
            for k in range(j):
                diff=an[j]-an[k]
                cd=an[k]
                while sum([0,0]<=cd)+sum(cd<pos.shape)==4:
                    anti.append(tuple(cd))
                    cd=cd-diff
                cd=an[j]
                while sum([0,0]<=cd)+sum(cd<pos.shape)==4:
                    anti.append(tuple(cd))
                    cd=cd+diff
tot=len(set(anti))
