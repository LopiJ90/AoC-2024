# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:44:18 2024

@author: hp
"""


import os
os.chdir(r'C:\Users\hp\Dropbox (Personale)\AoC')

import pandas as pd
import math
import numpy as np
with open('18.txt', 'r') as file:
    data = [tuple([int(i) for i in line.split(',')])for line in file.read().split('\n')]
A=71
B=71
maze=np.zeros(shape=(A,B))
#%%
for coo in data[:1024]:
    maze[coo]=1
#%%

import networkx as nx
G=nx.Graph()
for i in range(A):
    for j in range(B):
        if maze[i,j]==0:
            G.add_node((i,j))
            try:
                if maze[i+1,j]==0:
                    G.add_edge((i,j),(i+1,j))
            except:
                pass
            try:
                if maze[i,j+1]==0:
                    G.add_edge((i,j+1),(i,j))
            except:
                pass
#%%
nx.shortest_path_length(G, source=(0,0), target=(A-1,B-1), method='dijkstra')
#%%
import networkx as nx
G=nx.Graph()
for i in range(A):
    for j in range(B):
        G.add_node((i,j))
        G.add_edge((i,j),(i+1,j))
        G.add_edge((i,j+1),(i,j))
#%%
for coo in data:
    G.remove_node(coo)
    try:
        print(nx.shortest_path_length(G, source=(0,0), target=(A-1,B-1), method='dijkstra'))
    except:
        print(coo)
        break

