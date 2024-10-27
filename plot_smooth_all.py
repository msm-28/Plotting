#!/usr/bin/python

from matplotlib import pyplot as plt
import numpy as np
import matplotlib.cm as cm
import os
import re
from re import search
from random import randint
import sys

#filelist=[]

nsre = re.compile('([0-9]+)')
def sort_key(s):
    return[int(text) if text.isdigit() else text.lower() for text in re.split(nsre, s)]

filelist =sorted(os.listdir(os.getcwd()), key=sort_key)
filelist = [x for x in filelist if 'dat' in x]

n=7
out=["X", "ICL3","ICL32","PO4","CHOL"]
i=np.arange(1,5)
j=1

fig = plt.figure()
ax = fig.add_subplot(111)
#ax = fig.add_axes([0,0,1,1])
ax.set_xticks(np.arange(-6.0,8.0,2.0))
ax.set_yticks(np.arange(-0.2,2.0,0.2))
#ax.set_xticklabels(xlabels, Fontsize= )
#ax.tick_params(axis='x',size='3.0')

ax.set_xlim(-6,6)
ax.set_ylim(-0.2,1.8)
#plt.yticks(yt)
for axis in ['top', 'bottom', 'left', 'right']:
        ax.spines[axis].set_linewidth(1.5)
#ax.spines.set_linewidth(6)
#ax.legend(["complex","gm0","psgm0","popc-sm-chol","popc-chol","popc"])
colors1 = iter(cm.Blues_r(np.linspace(0, 1,n)))
colors2 = iter(cm.Purples_r(np.linspace(0, 1, n)))
colors3 = iter(cm.Oranges_r(np.linspace(0, 1, n)))
colors4 = iter(cm.Greens_r(np.linspace(0, 1, n)))

for fname in filelist:
    data=open(fname)
    lines = data.readlines()
    lines = [l.strip() for l in lines if not search ('[~!@#$%^&*]', l)]
    lines = np.array([l.split() for l in lines], dtype='float64')
    print(fname)

    X=lines[:,0]
    Y=lines[:,1]
    c=next(colors1)
    ax.plot(X,Y,linestyle='-',c=c)
#    leg = ax.legend(["complex","gm0","psgm0","popc-sm-chol","popc-chol","popc"])

    X=lines[:,0]
    Y=lines[:,2]
    c2=next(colors2)
    ax.plot(X,Y,linestyle='-.',c=c2)
#    leg = ax.legend(["complex","gm0","psgm0","popc-sm-chol","popc-chol","popc"])

    X=lines[:,0]
    Y=lines[:,3]
    c3=next(colors3)
    ax.plot(X,Y,linestyle='-',c=c3)
#    leg = ax.legend(["complex","gm0","psgm0","popc-sm-chol","popc-chol","popc"])

    X=lines[:,0]
    Y=lines[:,4]
    c4=next(colors4)
    ax.plot(X,Y,linestyle='-',c=c4)
#    leg = ax.legend(["complex","gm0","psgm0","popc-sm-chol","popc-chol","popc"])
    #leg = ax.legend()
   
    #plt.legend(["ROH"])
    #if j == 2:
    #    plt.plot(X,Y,linestyle='-',color='g')
    #print(out[1])
    #op = out + ".png" 
    
    plt.yticks(fontsize=13)
    plt.xticks(fontsize=13)
    plt.savefig("op.png",dpi=500,bbox_inches='tight')
    #print(j)
j = j + 1
#i = 1
