#!/usr/bin/env python

import numpy as np
import os
import re
from re import search
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import rc
import matplotlib as mpl
import sys
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

def plotmatrix(inu, out, title='', xl='', yl='', cbar=True):
    dirs = sorted(os.listdir(os.getcwd()))
    dirs = [x for x in dirs if '.xvg' in x]
    dirs = [x for x in dirs if inu in x] 
    maxim = 0
    for a in dirs:
        filename = open(os.getcwd()+'/'+a, 'r')
        lines = filename.readlines()
        filename.close()
        lines = [l.strip() for l in lines if not search('[@#$&*]', l)]
        if maxim < len(lines):
            maxim = len(lines)
    print '''The longest simulation period is : %d ps''' %  (maxim)
    mylist = np.reshape(np.zeros(maxim * len(dirs)), (maxim, len(dirs)))
    c = 0
    for b in dirs:
        filename = open(os.getcwd()+'/'+b, 'r')
        lines = filename.readlines()
        filename.close()
        lines = [l.strip() for l in lines if not search('[@#$*&]', l)]
        for d in np.arange(len(lines)):
            mylist[d][c] += float(lines[d].split()[1])

        c += 1
    mylist = np.transpose(mylist)
    print '''The closest point of approach between the two species is : %.4f nm''' % np.min(mylist)
    print '''The farthest distance between the two species is : %d nm''' % np.max(mylist)
    np.savetxt(out+'.dat', mylist)

    fig, ax = plt.subplots()
    xmajorLocator = MultipleLocator(5000)
#    majorFormatter = FormatStrFormatter('%d')
    minorLocator = MultipleLocator(1000)
    ax.set_title(title)
    ax.set_xlabel(xl)
    ax.set_ylabel(yl)
    mpl.rc('axes', linewidth=2)
    mpl.rcParams['xtick.minor.width'] = 2 
    plt.rcParams['axes.linewidth'] = 3 
    plt.rcParams['font.weight'] = 'bold'
    for axis in ['top', 'bottom', 'left', 'right']:
        ax.spines[axis].set_linewidth(3)
    #ax.set_xticks(0,20)
    #xla=[r'0', r'0', r'5', r'10', r'15', r'20', r'25', r'30', r'35', r'40', r'45',r'50',r'55',r'60',r'65']

    xla=[r'0', r'0', r'5',r'10', r'15', r'20',r'20']
#, r'40', r'50', r'60', r'70', r'80', r'90',r'100',r'110',r'120',r'130',r'140',r'150',r'160',r'170',r'180',r'190',r'200']
#    ax.set_xticklabels([r'0', r'0', r'5', r'10', r'15', r'20', r'25', r'30', r'35', r'40', r'45',r'50',r'55',r'60',r'65'],weight='bold')          
    ax.set_xticklabels(xla[0:10:1],weight='bold')          
#### Needs to be manually changed based on user requirement. Do not change the first entry (r'0')
    ax.set_yticks(np.linspace(0, len(mylist), len(mylist), endpoint=False)+0.5)
    ax.set_yticklabels([r'1', r'2', r'3', r'4', r'5', r'6', r'7', r'8', r'9', r'10',r'11',r'12',r'13',r'14',r'15',r'16'], weight='bold')                       #### Needs to be manually changed based on user requirement.
    ax.xaxis.set_major_locator(xmajorLocator)
#    ax.xaxis.set_major_formatter(majorFormatter)
    ax.xaxis.set_minor_locator(minorLocator)

    data = np.array(mylist, dtype='float64')
    max = np.max(data)
    min = np.min(data) 
    im = ax.pcolormesh(data, cmap=cm.jet, vmin=0, vmax=max)

    ax.tick_params(axis='x', color='black',
        length=6, width=2, labelsize=6, direction='in',
        bottom='on', left='on', top='off', right='off',
        labelbottom='on', labelleft='on', labeltop='off', labelright='off')
    ax.tick_params(axis='y', color='black', 
        length=6, width=2, labelsize=12, direction='in',
        bottom='off', left='on', top='on', right='off',
        labelbottom='off', labelleft='on', labeltop='on', labelright='off')

    if cbar:
       cb=fig.colorbar(im, orientation='horizontal', format="%s")
       cb.set_label(r'Distance (nm)', size=14, weight='bold')
       cb.ax.tick_params(labelsize=10, length=6, width=2)
    plt.savefig(out+'.png', transparent=True, dpi=200)                                                                   #### default is .png. You can change it to .svg too.

if len(sys.argv) != 3:
    print 'M> Usage: python demo.py file out'
    sys.exit()

try:
    inu = sys.argv[1]
    out = sys.argv[2]
except:
    print 'E> Failed due one or several errors: '
    print '\t Reading file, parsing args'
    raise
    sys.exit()
try:
    plotmatrix(inu, out, '', 'Time (us)', 'Simulation Number')
    if os.path.isfile(out+'.png'):
        print 'M> "%s" and "%s" are generated' % (out+'.dat', out+'.png')
except:
    print 'E> Something went wrong'
    raise
