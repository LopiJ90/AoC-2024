# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 11:14:40 2024

@author: lopif
"""

import os

os.chdir(r'C:\Users\lopif\OneDrive\Documenti\AoC')
import pandas as pd
import numpy as np
import math
from tqdm import tqdm
with open('13.txt', 'r') as file:
    data = file.read()

data=[[k for k in pr.split()] for pr in data.split('\n\n')]

#%%
coin=0
for prob in data:
    steps=np.array([[int(prob[2][2:-1]),int(prob[6][2:-1])],[int(prob[3][2:]),int(prob[7][2:])]])
    res=np.array([int(prob[9][2:-1]),int(prob[10][2:])])
    res=res+[10000000000000,10000000000000]
    vals=np.linalg.solve(steps,res)
    if abs(vals[0]-round(vals[0]))+abs(vals[1]-round(vals[1]))<0.0001:
        coin=coin+3*round(vals[0])
        coin=coin+round(vals[1])
    print(vals[0],vals[1])
#%%