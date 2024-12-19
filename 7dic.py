# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 10:25:43 2024

@author: lopif
"""

import os

os.chdir(r'C:\Users\lopif\OneDrive\Documenti\AoC')
import pandas as pd
from tqdm import tqdm
with open('07.txt', 'r') as file:
    data = file.read()

lines=[i.split() for i in data.split('\n')]
for i in lines:
    i[0]=i[0][:-1]
    
    
A=len(lines)

for i in range(A):
    lines[i]=[int(i) for i in lines[i]]

#%%
tot=0
for line in tqdm(lines):
    num=0
    A=len(line)
    form='#'+str(A+1)+'b'
    while num<2**(A-1):
        check=list(format(num, form))[2:]
        val=line[1]
        for j in range(A-2):
            if check[j]=='1':
                val=val+line[j+2]
            else:
                val=val*line[j+2]
        if val== line[0]:
            tot+=line[0]
            break
        num+=1
        
#%%

import numpy as np
import math

tot=0
for line in tqdm(lines):
    num=0
    A=len(line)
    while num<3**(A-2):
        check=np.base_repr(num,3)
        check='0'*(A-2-len(check))+check
        val=line[1]
        for j in range(A-2):
            if check[j]=='0':
                val=int(str(val)+str(line[j+2]))
            elif check[j]=='1':
                val=val+line[j+2]
            else:
                val=val*line[j+2]
        if val== line[0]:
            tot+=line[0]
            break
        num+=1
