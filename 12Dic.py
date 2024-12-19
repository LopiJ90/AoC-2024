# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 10:16:40 2024

@author: lopif
"""

import os

os.chdir(r'C:\Users\lopif\OneDrive\Documenti\AoC')
import pandas as pd
import numpy as np
from tqdm import tqdm
import copy
with open('12.txt', 'r') as file:
    data = file.read()

lines=[list(i) for i in data.split('\n')]

lines=np.array(lines,dtype=str)
#%%

A,B=lines.shape
tot=0
glo=0
removed=copy.deepcopy(lines)
for i in range(A):
    for j in range(B):
        if removed[i,j]=='0':
            pass
        else:
            curr=set()
            succ=set()
            succ.add((i,j))
            tot=set()
            tot.add((i,j))

            val=lines[i,j]
            while len(succ)>0:
                curr=succ
                succ=set()
                for coo in curr:
                    nei=[(coo[0],coo[1]+1),(coo[0],coo[1]-1),(coo[0]+1,coo[1]),(coo[0]-1,coo[1])]
                    nei=[t for t in nei if 0<=t[0]<A and 0<=t[1]<B and lines[t]==val and t not in tot]
                    succ=succ.union(set(nei))

                tot=tot.union(succ)
            per=0
            for coo in tot:
                removed[coo]='0'
                nei=[(coo[0],coo[1]+1),(coo[0],coo[1]-1),(coo[0]+1,coo[1]),(coo[0]-1,coo[1])]

                nei=[t for t in nei if  t not in tot]

                per+=len(nei)
            glo+=len(tot)*per
            
#%%

A,B=lines.shape
tot=0
glo=0
removed=copy.deepcopy(lines)
for i in range(A):
    for j in range(B):
        if removed[i,j]=='0':
            pass
        else:
            curr=set()
            succ=set()
            succ.add((i,j))
            tot=set()
            tot.add((i,j))

            val=lines[i,j]
            while len(succ)>0:
                curr=succ
                succ=set()
                for coo in curr:
                    nei=[(coo[0],coo[1]+1),(coo[0],coo[1]-1),(coo[0]+1,coo[1]),(coo[0]-1,coo[1])]
                    nei=[t for t in nei if 0<=t[0]<A and 0<=t[1]<B and lines[t]==val and t not in tot]
                    succ=succ.union(set(nei))

                tot=tot.union(succ)
                bound=set()
            for coo in tot:
                removed[coo]='0'
                nei=[(coo[0],coo[1]+1),(coo[0],coo[1]-1),(coo[0]+1,coo[1]),(coo[0]-1,coo[1])]

                nei=[t for t in nei if  t not in tot]
                bound=bound.union(set([(coo,t) for t in nei]))
            newbound=copy.deepcopy(bound)
            side=0

            for b in bound:
                if b in newbound:
                    up=b
                    while up in bound:
                        up=((up[0][0]-1,up[0][1]),(up[1][0]-1,up[1][1]))
                        try:
                            newbound.remove(up)
                        except:
                            pass
                    up=b
    
                    while up in bound:
                        up=((up[0][0]+1,up[0][1]),(up[1][0]+1,up[1][1]))
                        try:
                            newbound.remove(up)
                        except:
                            pass
                    up=b
    
                    while up in bound:
                        up=((up[0][0],up[0][1]+1),(up[1][0],up[1][1]+1))
                        try:
                            newbound.remove(up)
                        except:
                            pass
                    up=b
    
                    while up in bound:
                        up=((up[0][0],up[0][1]-1),(up[1][0],up[1][1]-1))
                        try:
                            newbound.remove(up)
                        except:
                            pass
                    side+=1
            print(val, len(tot), side)
            glo+=len(tot)*side

