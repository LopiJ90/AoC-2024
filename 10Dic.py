# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:15:54 2024

@author: lopif
"""

import os

os.chdir(r'C:\Users\lopif\OneDrive\Documenti\AoC')
import pandas as pd
import numpy as np
from tqdm import tqdm
with open('10.txt', 'r') as file:
    data = file.read()

lines=[list(i) for i in data.split('\n')]

lines=np.array(lines,dtype=int)
#%%
A,B=lines.shape
tot=0
question=1
for i in range(A):
    for j in range(B):
        curr=[]
        succ=[]
        succ.append((i,j))
        if lines[i,j]!=0:
            pass
        else:
            for k in range(1,10):
                curr=succ
                succ=[]
                for coo in curr:
                    nei=[(coo[0],coo[1]+1),(coo[0],coo[1]-1),(coo[0]+1,coo[1]),(coo[0]-1,coo[1])]
                    nei=[t for t in nei if 0<=t[0]<A and 0<=t[1]<B]
                    succ.extend([c for c in nei if lines[c]==k])
            if question==2:
                tot+=len(succ)
                print(succ)
            elif question==1:
                tot+=len(set(succ))
