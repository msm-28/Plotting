#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
plotmatrix.py
  Plots a matrix using matplotlib
  Input file must have 3 columns
  Based on the standard matplotlib example: matshow.py
     See: http://matplotlib.org/examples/pylab_examples/matshow.html
"""

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from matplotlib import colors
from numpy.random import random_integers
from numpy import min, max, genfromtxt, linspace
import sys

#MMSEQ = ['2', '4', '6', '8']#y 
#TMSEQ = ['15', '30', '45', '60', '75', '90', '105'] #x
TMSEQ = ['I','II','III','IV','V','VI','VII','162','163','164','165','166','167','168','169','170','171','172','173','174','175'] #y axis
MMSEQ = ['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100','125','345','346','347','348','349','350','351','352','353','354','355','356','357','358','359','360','361','362','363','364','365'] #x axis
#['40','60','80','100', '120', '140','160','180','200','220','240','260','280','300','320','340','360']# '90'] #'100', '110#', '120', '130', '140', '150', '160', '170', '180', '190', '200', '210', '220', '230', '240', '250', '260', '270', '280', '290', '300']


#SEQTM = TMSEQ[::-1]

#this screws up the original array?
#SEQTM = TMSEQ
#SEQTM.reverse()
#

#global properties
plt.rcParams['font.size'] = 30
plt.rcParams['font.family'] = 'monospace'
plt.rcParams['figure.figsize'] = 20,20 

def plotmatrix(data, png, title='', xl='', yl='', cbar=True,
               interpol='nearest', vmin=0.0, vmax=1.0, 
               cmap=cm.bone_r, norm=None):
    """ plots matrix with title, labels and optional color bar"""
    fig, ax = plt.subplots()

    im = ax.imshow(data, cmap=cmap, interpolation=interpol,
                  vmin=vmin, vmax=vmax, aspect=1.0, 
                  origin='lower', norm=norm)
    ax.set_title(title)  
    ax.set_xlabel(xl, weight = 'bold')
    ax.set_ylabel(yl, weight = 'bold')
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(5.0)
#    ax.grid(True, color=(0.1, 0.1, 0.1), linestyle='-', alpha=0.5, lw=0.5)
#    ax.set_xlim([0, 500])
#    ax.set_ylim([0, 16])
    ax.tick_params(axis='both', width=2, pad=30, length=10,labelsize=14.0)
#    plt.xticks(range(50), TMSEQ + TMSEQ, va = 'baseline')
#    plt.yticks(range(50), TMSEQ + TMSEQ, ha ='left')
    plt.xticks(range(0,20,10000),  va = 'baseline', weight='bold') # range(0,375,25) means it will always start from 0, till number of POPC-N, sepe#rated by a distance of 25 on X-axis 
    plt.yticks(range(0,16,1), ha = 'left', weight='bold')   
   
    if cbar:
        cb = fig.colorbar(im, orientation='horizontal', format="%.2f")#,
        #ticks=[0,0.1,0.2,0.3,0.4,0.5]) #numbers on the scale color bar
	
    plt.savefig(png, format='png', dpi=300, transparent=True)


if len(sys.argv) != 3:
    print 'M> usage: plotmatrix.py matrix.dat  matrix.png'
    sys.exit()

try:
    f = sys.argv[1]
    png = sys.argv[2]
    mtrx = genfromtxt(f, autostrip=True, usemask=False, comments='#',
                        skiprows=0, skip_header=0, skip_footer=0,
                        invalid_raise=True)
    print np.shape(mtrx)
    print 'M> Read matrix of shape: "{0}"'.format(mtrx.shape)
    mtrx.astype('float64')
    t = mtrx[0:200000, 0:16]
    mn = min(t)
    mx = max(t)
    print(mn)
    print(mx)
#  custom cmap
#http://stackoverflow.com/questions/9707676/
#http://matplotlib.org/examples/api/colorbar_only.html
    
    mycmap = colors.ListedColormap(['white', '#FFFFBB', '#C3FDB8', '#B5EAAA', '#64E986', '#54C571'])
#    h = [(1, 1, 1, 0.5), (1, 1, 1, 1.0), (1, 1, 0, 0.5), (1, 1, 0, 1.0),
#         (1, 0, 0, 0.5), (1, 0, 0, 1.0), (0, 0, 0, 0.5), (0, 0, 0, 1.0)]
#    mycmap = colors.ListedColormap(h)
#    mycmap.set_over('black')
#    mycmap.set_under('white')
#    bounds = [0, 0.15,0.30,0.45,0.60,0.75,0.90]
#    norm = colors.BoundaryNorm(bounds, mycmap.N)

#   No need to transpose, symmetric matrix    
#    print mtrx == mtrx.T
#    plotmatrix(t, png, vmin=0.0, vmax=1.0, xl='chainA', 
#               yl='chainB', cmap=cm.gist_yarg)
    plotmatrix(t, png, xl='', yl='', cmap=cm.jet,vmin=vmin, vmax=vmax)
except:
    print 'E> Failed due to one or several errors, last error was:\n \
           "{0:*^50s}"'.format(sys.exc_info()[1])
    sys.exit()
