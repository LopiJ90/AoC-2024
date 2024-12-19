# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 10:52:45 2024

@author: lopif
"""

import os

os.chdir(r'C:\Users\lopif\OneDrive\Documenti\AoC')
import pandas as pd
import numpy as np
from tqdm import tqdm
import copy
with open('15pr.txt', 'r') as file:
    data = file.read()
    

splitdata=data.split("\n\n")

lines=np.array([list(i) for i in splitdata[0].split('\n')])
moves=list(splitdata[1])
linestart=copy.deepcopy(lines)

import seaborn as sns
from matplotlib import pyplot as plt

import pylab as pl

#%%
lines=np.array([list(i) for i in splitdata[0].split('\n')])

start=np.where(lines=='@')
start=(start[0][0],start[1][0])
curr=start
lines[start]='.'
movedict={'^':(-1,0),'>':(0,1),'<':(0,-1),'v':(1,0)}
for i,step in enumerate(moves):
    try:
        print(i,step)
        dire=movedict[step]
        succ=(curr[0]+dire[0],curr[1]+dire[1])
        if lines[succ]=='.':
            curr=succ
        elif lines[succ]=='#':
            pass
        elif lines[succ]=='O':
            while lines[succ]=='O':
                succ=(succ[0]+dire[0],succ[1]+dire[1])
            if lines[succ]=='#':
                pass
            elif lines[succ]=='.':
               lines[(curr[0]+dire[0],curr[1]+dire[1])]='.'
               curr =(curr[0]+dire[0],curr[1]+dire[1])

               lines[succ]='O'
    except:
        pass
    print(succ,curr)
boxes=np.where(lines=='O')
 
tot=np.sum(boxes[0])*100+np.sum(boxes[1])

#%%

os.chdir(r'C:\Users\lopif\OneDrive\Documenti\AoC\PlottiniPuccettini')
plotdict={'#':0,'.':100,'[':40,']':40,'@':60}

newlines=[]
labdict={'.':['.','.'],'#':['#','#'],'@':['@','.'],'O':['[',']']}

for i,line in enumerate(lines):
    newlines.append([])
    for j in line:
        newlines[i].extend(labdict[j])
newlines=np.array(newlines)

newlinestart=copy.deepcopy(newlines)

start=np.where(newlines=='@')
start=(start[0][0],start[1][0])
curr=start
newlines[start]='.'

movedict={'^':(-1,0),'>':(0,1),'<':(0,-1),'v':(1,0)}
for i,step in enumerate(moves):
    newlines[curr]='@'
    to_plot=np.zeros((10,20))
    for k in range(10):
        for l in range(20):
            to_plot[k,l]=plotdict[newlines[k,l]]
    newlines[curr]='.'
    fig=plt.figure(i)
    ax = plt.axes()

    sns.heatmap(to_plot,ax=ax,cbar=False)
    ax.set_title(i)
    fig.add_axes(ax)
    name=str(i).rjust(3, '0')+'step.jpg'
    pl.figure(i)
    plt.savefig(name,format='jpg')

    plt.show(fig)

    try:

        oldlines=copy.deepcopy(newlines)
        to_move=[]
        dire=movedict[step]

        if dire[0]==0:
            succ=(curr[0]+dire[0],curr[1]+dire[1])
            if newlines[succ]=='.':
                curr=succ
            elif newlines[succ]=='#':
                pass
            elif newlines[succ] in set(['[',']']):
                to_move=set([succ])
                while newlines[succ]in set(['[',']']):
                    succ=(succ[0]+dire[0],succ[1]+dire[1])
                    to_move.add(succ)
                    
                if newlines[succ]=='#':
                    pass
                elif newlines[succ]=='.':
                    curr =(curr[0]+dire[0],curr[1]+dire[1])
                    for pos in to_move:
                        if (pos[0]-dire[0],pos[1]-dire[1]) in to_move:
                            newlines[pos]=oldlines[pos[0]-dire[0],pos[1]-dire[1]]
                        else:
                            newlines[pos]='.'
        elif dire[1]==0:
            succ=(curr[0]+dire[0],curr[1]+dire[1])
            if newlines[succ]=='.':
                curr=succ
            elif newlines[succ]=='#':
                pass
            elif newlines[succ] in set(['[',']']):
                to_move=set([succ])
                if newlines[succ]=='[':
                    to_move.add((succ[0],succ[1]+1))

                else:
                    to_move.add((succ[0],succ[1]-1))
                    
                check=to_move
                err=0
                nextcheck=check
                while len(nextcheck)>0:
                    

                    nextcheck=set()
                    for pos in check:
                        if oldlines[pos] in ['[',']']:
                            nextcheck.add((pos[0]+dire[0],pos[1]))
                            if oldlines[pos[0]+dire[0],pos[1]]=='[':
                                nextcheck.add((pos[0]+dire[0],pos[1]+1))
                            elif oldlines[pos[0]+dire[0],pos[1]]==']':
                                nextcheck.add((pos[0]+dire[0],pos[1]-1))
                        elif oldlines[pos]=='#':
                            err=1
                    if err==1:
                        break
                    else:
                        to_move=to_move.union(nextcheck)
                        check=nextcheck
                if err ==0:

                    curr =(curr[0]+dire[0],curr[1]+dire[1])
                    for pos in to_move:
                        if (pos[0]-dire[0],pos[1]-dire[1]) in to_move:
                            newlines[pos]=oldlines[pos[0]-dire[0],pos[1]-dire[1]]
                        else:
                            newlines[pos]='.'
                    





    except:
        print(i, step)
boxes=np.where(newlines=='[')
 
tot=np.sum(boxes[0])*100+np.sum(boxes[1])
#%%

d=oldlines==oldlinesOr
e=newlines==newlinesOr

#%%
plotdict={'#':0,'.':100,'[':45,']':40,'@':60}

newlinestart[curr]='@'
to_plot=np.zeros((50,100))
for k in range(50):
    for l in range(100):
        to_plot[k,l]=plotdict[newlinestart[k,l]]
newlines[curr]='.'
 
ax = plt.axes()

sns.heatmap(to_plot,ax=ax)
ax.set_title(i)
plt.show()
