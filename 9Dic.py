# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:04:26 2024

@author: lopif
"""

import os

os.chdir(r'C:\Users\lopif\OneDrive\Documenti\AoC')
import pandas as pd
from tqdm import tqdm

with open('09.txt', 'r') as file:
    data = file.read()
#%%

data='2333133121414131402'

#%%

nums=[int(i) for i in data]
vals=[]
A=len(nums)
for i in range(A):
    if i%2==0:
        vals.extend([round(i/2)]*nums[i])
    else:
        vals.extend(['.']*nums[i])


#%%
import numpy as np
vals=np.array(vals)
c1=0
c2=vals.size-1

while c1<=c2:
    while vals[c1]!='.':
        c1+=1
    while vals[c2]=='.':
        c2-=1
    if c1<c2:
        vals[[c1,c2]]=vals[[c2,c1]]
        print(c1,c2)
    c1+=1
    c2-=1
#%%
vals[vals=='.']=0
vals=np.array(vals, dtype=float)
checksum=np.dot(vals,np.array(range(vals.size)))

#%%
nums=[int(i) for i in data]
vals=[]
A=len(nums)
for i in range(A):
    if i%2==0:
        vals.extend([round(i/2)]*nums[i])
    else:
        vals.extend(['.']*nums[i])

#%%

n2=A-1
vals=np.array(vals)

while n2>0:
    ns=sum(nums[:n2])
    dots=0
    for i in range(ns):
        if vals[i]=='.':
            dots+=1
        else:
            dots=0
        if dots==nums[n2]:
            list1=list(range(i-nums[n2]+1,i+1))
            list1.extend(list(range(ns,ns+nums[n2])))
            list2=list(range(ns,ns+nums[n2]))
            list2.extend(list(range(i-nums[n2]+1,i+1)))
            vals[list1]=vals[list2]
            break
    n2-=2
    print(n2)
        

#%%

vals[vals=='.']=0
vals=np.array(vals, dtype=float)
checksum=np.dot(vals,np.array(range(vals.size)))
#%%

while c1<c2:
    if nums[c2]<=nums[c1]:
       swaps[c1]=c2
       c1+=2
       c2-=2
    else:
        c2-=2
    print(c1,c2)


