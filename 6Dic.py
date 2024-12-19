# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 13:28:45 2024

@author: lopif
"""

import os

os.chdir(r'C:\Users\lopif\OneDrive\Documenti\AoC')
import pandas as pd
from tqdm import tqdm
with open('06.txt', 'r') as file:
    data = file.read()

lines=[list(i) for i in data.split('\n')]

A=len(lines)
B=len(lines[0])


for i in range(A):
    for j in range(B):
        if lines[i][j]=='^':
            start=[i,j,0]
            lines[i][j]='.'
        if lines[i][j]=='>':
            start=[i,j,1]
            lines[i][j]='.'
        if lines[i][j]=='v':
            start=[i,j,2]
            lines[i][j]='.'
        if lines[i][j]=='<':
            start=[i,j,3]
            lines[i][j]='.'
#%%

pos=start


while True:
    lines[pos[0]][pos[1]]='X'
    if pos[2]==0:
        if lines[pos[0]-1][pos[1]]=='#':
            pos[2]=(pos[2]+1)%4
        else:
            pos[0]=pos[0]-1
    if pos[2]==1:
        if lines[pos[0]][pos[1]+1]=='#':
            pos[2]=(pos[2]+1)%4
        else:
            pos[1]=pos[1]+1
    if pos[2]==2:
        if lines[pos[0]+1][pos[1]]=='#':
            pos[2]=(pos[2]+1)%4
        else:
            pos[0]=pos[0]+1
    if pos[2]==3:
        if lines[pos[0]][pos[1]-1]=='#':
            pos[2]=(pos[2]+1)%4
        else:
            pos[1]=pos[1]-1


#%%

tot=sum([line.count('X') for line in lines])
#%%
import numpy as np
import copy
linAr=np.array(lines)
bad=0
bads=[]
steps=[[-1,0],[0,1],[1,0],[0,-1]]
for k in range(A):
    print(k)
    for l in tqdm(range(B)):
        if [k,l] != start[:2]:
            linNow=copy.deepcopy(linAr)
            linSave=[copy.deepcopy(linAr),copy.deepcopy(linAr),copy.deepcopy(linAr),copy.deepcopy(linAr)]

            linNow[k,l]='#'
            pos=np.array(start)
            tar=copy.deepcopy(pos[:2])
            while True:
                #visited.append(copy.deepcopy(pos))

                linSave[pos[2]][pos[0],pos[1]]='X'
                tar=pos[:2]+steps[pos[2]]
                if(0<= tar[0]< A) and (0<= tar[1]<B):
                    if linNow[tar[0],tar[1]]=='#':
                        pos[2]=(pos[2]+1)%4
                    else: 
                        pos[:2]=tar
                else:
                    break
                if linSave[pos[2]][pos[0],pos[1]]=='X':
                    bad+=1
                    bads.append([k,l])
                    break
                
                    
                    


                #%%
visited.append(pos)

pos in visited
#%%
unique, counts=np.unique(linNow, return_counts=True)
tot= dict(zip(unique, counts))['X']
