# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 11:34:39 2024

@author: lopif
"""

import os

os.chdir(r'C:\Users\lopif\OneDrive\Documenti\AoC')
import pandas as pd
import numpy as np
import math
from tqdm import tqdm
with open('14.txt', 'r') as file:
    data = file.read()

data=[[k for k in pr.split()] for pr in data.split('\n')]
#%%
A=len(data)
desc=np.zeros((A,4))
for i,line in enumerate(data):
    posvel=np.zeros(4)
    posvel[0]=line[0].split('=')[1].split(',')[0]
    posvel[1]=line[0].split('=')[1].split(',')[1]
    posvel[2]=line[1].split('=')[1].split(',')[0]
    posvel[3]=line[1].split('=')[1].split(',')[1]
    desc[i,:]=posvel
#%%
lenx=101
leny=103
posfin=np.zeros((len(data),2))

for i in range(A):
    posfin[i,0]=(desc[i,0]+100*desc[i,2])%lenx
    posfin[i,1]=(desc[i,1]+100*desc[i,3])%leny
#%%
cutx=math.floor(lenx/2)
cuty=math.floor(leny/2)

q2=sum([posfin[i,0]<cutx and posfin[i,1]<cuty for i in range(A)])
q1=sum([posfin[i,0]<cutx and posfin[i,1]>cuty for i in range(A)])
q4=sum([posfin[i,0]>cutx and posfin[i,1]<cuty for i in range(A)])
q3=sum([posfin[i,0]>cutx and posfin[i,1]>cuty for i in range(A)])

tot=q1*q2*q3*q4
#%%
import seaborn as sns
from matplotlib import pyplot as plt
to_plot=np.zeros((lenx,leny))


start=desc[:,:2]
vel=desc[:,2:]
for k in range(7343,7345):
    pos=start+k*vel
    pos[:,0]=pos[:,0]%lenx
    pos[:,1]=pos[:,1]%leny

    to_plot=np.zeros((lenx,leny))
    for i in range(A):
        to_plot[round(pos[i,0]),round(pos[i,1])]=1
    ax = plt.axes()

    sns.heatmap(to_plot,ax=ax)
    ax.set_title(k)
    plt.show()