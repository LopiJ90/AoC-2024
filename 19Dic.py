# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 19:18:02 2024

@author: lopif
"""

import os

os.chdir(r'C:\Users\lopif\OneDrive\Documenti\AoC')
import pandas as pd
import numpy as np
from tqdm import tqdm
import copy
with open('19.txt', 'r') as file:
    data = file.read()
    

splitdata=data.split("\n\n")
#%%

val=splitdata[0].split(', ')

lines=splitdata[1].split('\n')

#%%
tot=0

for i, line in tqdm(enumerate(lines)):
    tails=[line]
    newtails=set()
    while len(tails)>0:
        for v in val:
            for t in tails:
                if t.startswith(v):
                    newtails.add(t[len(v):])
        tails=newtails
        newtails=set()
        
        if '' in tails:
            tot+=1
            break
#%%

tot=0

for i, line in tqdm(enumerate(lines)):
    print(line)
    tails=pd.Series([1],index=[line])
    newtails=pd.Series()
    while len(tails)>0:
        for v in val:
            for t in tails.index:
                if t.startswith(v):
                    if t[len(v):] not in newtails.index:
                        newtails[t[len(v):]]=tails[t]
                    else:
                        newtails[t[len(v):]]+=tails[t]
        tails=newtails
        newtails=pd.Series()
        
        if '' in tails.index:
            tot+=tails['']
    print(tot)
