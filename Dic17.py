# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 14:02:21 2024

@author: hp
"""

import os
os.chdir(r'C:\Users\hp\Dropbox (Personale)\AoC')

import pandas as pd
import math
with open('17.txt', 'r') as file:
    data = file.read().split('\n')
    
    
#%%

cmb=[0,1,2,3,int(data[0].split()[-1]),int(data[1].split()[-1]),int(data[2].split()[-1])]
cnd=[int(i[-1]) for i in data[-1].split(',')]


poi=0
out=[]
while poi<len(cnd)-1:
    if cnd[poi]==0:
        cmb[4]=math.floor(cmb[4]/2**cmb[cnd[poi+1]])
        poi+=2
    elif cnd[poi]==1:
        cmb[5]=cmb[5]^cnd[poi+1]
        poi+=2
    elif cnd[poi]==2:
        cmb[5]=cmb[cnd[poi+1]]%8
        poi+=2
    elif cnd[poi]==3:
        if cmb[4]==0:
            poi+=2
        else:
            poi=cnd[poi+1]
    elif cnd[poi]==4:
        cmb[5]=cmb[5]^cmb[6]
        poi+=2
    elif cnd[poi]==5:
        out.append(str(cmb[cnd[poi+1]]%8))
        poi+=2
    elif cnd[poi]==6:
        cmb[5]=math.floor(cmb[4]/2**cmb[cnd[poi+1]])
        poi+=2
    elif cnd[poi]==7:
        cmb[6]=math.floor(cmb[4]/2**cmb[cnd[poi+1]])
        poi+=2
    try:
        print(cnd[poi],cmb[4:])
    except:
        pass
#%%
fin=','.join(out)
#%%
def prog(A,comm):
    cmb=[0,1,2,3,A,0,0]    
    poi=0
    out=[]
    while poi<len(comm)-1:
        if comm[poi]==0:
            cmb[4]=math.floor(cmb[4]/2**cmb[comm[poi+1]])
            poi+=2
        elif comm[poi]==1:
            cmb[5]=cmb[5]^comm[poi+1]
            poi+=2
        elif comm[poi]==2:
            cmb[5]=cmb[comm[poi+1]]%8
            poi+=2
        elif comm[poi]==3:
            if cmb[4]==0:
                poi+=2
            else:
                poi=comm[poi+1]
        elif comm[poi]==4:
            cmb[5]=cmb[5]^cmb[6]
            poi+=2
        elif comm[poi]==5:
            out.append(cmb[comm[poi+1]]%8)
            poi+=2
        elif comm[poi]==6:
            cmb[5]=math.floor(cmb[4]/2**cmb[comm[poi+1]])
            poi+=2
        elif comm[poi]==7:
            cmb[6]=math.floor(cmb[4]/2**cmb[comm[poi+1]])
            poi+=2
        # try:
        #     print(comm[poi],cmb[4:])
        # except:
        #     pass
        # if len(out)>len(comm):
        #     break
    return out

#%%
poss=[[]]
for i in range(8):
    if prog(i,cnd)==cnd[-1:]:
        poss[0].append(i)
for i in range(1,16):
    poss.append([])
    for k in poss[i-1]:
        for j in range(8):
            if prog(k*8+j,cnd)==cnd[-(i+1):]:
                poss[i].append(k*8+j)
print(min(poss[15]))