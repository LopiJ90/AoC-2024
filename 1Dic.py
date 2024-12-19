# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 13:16:11 2024

@author: lopif
"""

import pandas as pd


data=pd.read_csv(r'C:\Users\lopif\OneDrive\Documenti\AoC\011.csv',sep='  ',names=['A','B'])


#%%

dataS=pd.DataFrame(columns=['A','B'])

dataS['A']=data['A'].sort_values()
#%%


dataVal=data['B'].value_counts().reset_index()

dataVal=dataVal[dataVal['B'].isin(data['A']) ]
#%%

dataVal['C']=dataVal['B']*dataVal['count']
dataVal['C'].sum()
