# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 18:54:35 2024

@author: hp
"""
import os
os.chdir(r'C:\Users\hp\Dropbox (Personale)\AoC')

import pandas as pd

with open('16.txt', 'r') as file:
    data = file.read()
import numpy as np
maze=np.array([list(line) for line in data.split('\n')])

#%%

A,B=maze.shape

#%%

start=np.where(maze=='E')
end=np.where(maze=='S')
maze[start]='.'
maze[end]='.'

directions=['^','<','>','v']
#%%
import networkx as nx
G=nx.DiGraph()
for i in range(A):
    for j in range(B):
        if maze[i,j]=='.':
            to_add=[(i,j,'^'),(i,j,'>'),(i,j,'v'),(i,j,'<')]
            to_add_edges=[((i,j,'^'),(i,j,'>')),((i,j,'>'),(i,j,'^')),
                         ((i,j,'>'),(i,j,'v')),((i,j,'v'),(i,j,'>')),
                         ((i,j,'<'),(i,j,'v')),((i,j,'v'),(i,j,'<')),
                         ((i,j,'<'),(i,j,'^')),((i,j,'^'),(i,j,'<'))]
            G.add_nodes_from(to_add)
            G.add_edges_from(to_add_edges,length=1000)

for i in range(A):
    for j in range(B):
        if maze[i,j]=='.':
            if maze[i,j+1]=='.':
                G.add_edge((i,j,'>'),(i,j+1,'>'),length=1)                
            if maze[i,j-1]=='.':
                G.add_edge((i,j,'<'),(i,j-1,'<'),length=1)                
            if maze[i-1,j]=='.':
                G.add_edge((i,j,'^'),(i-1,j,'^'),length=1)                
            if maze[i+1,j]=='.':
                G.add_edge((i,j,'v'),(i+1,j,'v'),length=1)
#%%                
nx.shortest_path_length(G, source=(start[0][0],start[1][0],'>'), target=(end[0][0],end[1][0],'v'), weight='length', method='dijkstra')
#%%

minim=set().union(*[set(i) for i in nx.all_shortest_paths(G, source=(start[0][0],start[1][0],'>'), target=(end[0][0],end[1][0],'v'), weight='length', method='dijkstra')])


minpos=set([i[:2] for i in minim])