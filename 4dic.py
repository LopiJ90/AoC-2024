# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:58:04 2024

@author: lopif
"""

import os

os.chdir(r'C:\Users\lopif\OneDrive\Documenti\AoC')
import pandas as pd

with open('04.txt', 'r') as file:
    data = file.read()
    
mults=data.split('\n')

#%%
xmas=0

for i in range(140):
    for j in range(140):
        try:
            if mults[i][j]+mults[i][j+1]+mults[i][j+2]+mults[i][j+3]=='XMAS':
                xmas+=1
        except:
            pass
        try:
            if j>2 and mults[i][j]+mults[i][j-1]+mults[i][j-2]+mults[i][j-3]=='XMAS':
                xmas+=1
        except:
            pass
        try:
            if mults[i][j]+mults[i+1][j]+mults[i+2][j]+mults[i+3][j]=='XMAS':
                xmas+=1
        except:
            pass
        try:
            if i>2 and mults[i][j]+mults[i-1][j]+mults[i-2][j]+mults[i-3][j]=='XMAS':
                xmas+=1
        except:
            pass

        try:
            if mults[i][j]+mults[i+1][j+1]+mults[i+2][j+2]+mults[i+3][j+3]=='XMAS':
                xmas+=1  
        except:
            pass
        try:
            if i>2 and j>2 and mults[i][j]+mults[i-1][j-1]+mults[i-2][j-2]+mults[i-3][j-3]=='XMAS':
                xmas+=1
                print(i,j)
        except:
            pass

        try:
            if j> 2 and mults[i][j]+mults[i+1][j-1]+mults[i+2][j-2]+mults[i+3][j-3]=='XMAS':
                xmas+=1
        except:
            pass
        try:
            if i>2 and mults[i][j]+mults[i-1][j+1]+mults[i-2][j+2]+mults[i-3][j+3]=='XMAS':
                xmas+=1
        except:
            pass
#%%

i=9
j=1

#%%

mults[i][j]+mults[i-1][j-1]+mults[i-2][j-2]+mults[i-3][j-3]

#%%
xmas=0

valid=['MMSS','SMMS','MSSM','SSMM']

for i in range (1,139):
    for j in range(1,139):
        if mults[i][j]=='A':
            if mults[i+1][j+1]+mults[i+1][j-1]+mults[i-1][j-1]+mults[i-1][j+1] in valid:
                xmas+=1
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            