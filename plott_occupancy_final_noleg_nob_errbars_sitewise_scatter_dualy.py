#! usr/bin/env python

#Maxnormalized the input occupancy data and then plot 
#Can process individual .dat files for plotting
import numpy as np
import os
import re
from re import search
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

nsre = re.compile('([0-9]+)')
error_config = {'ecolor': '0.5'}
#error_11= (0.011967031,	0.052035861,	0.015301899,	0.03786735,	0.046621448,	0.099768305,	0.010955834)
#error_1=(0.061151853,	0.098024924,	0.164472068,	0.093041836,	0.161066204,	0.089685768,	0.064119679)
N = 9
def sort_key(s):
    return[int(text) if text.isdigit() else text.lower() for text in re.split(nsre, s)]

files = sorted(os.listdir(os.getcwd()), key=sort_key)
files = [x for x in files if 'dat' in x]
print files
for i in np.arange(len(files)):
	filename = open(os.getcwd()+'/'+files[i], 'r')
	nam=files[i].split('.')
	fna= nam[0]
	fna=fna +'_avg_y'+'.png'
	#ylab=nam[0]+'-Occupancy'
	#ttl=ylab+' for each helix'
#	print "**"
	lines = filename.readlines()
	filename.close()
	
	mat1 = np.zeros(len(lines[0].split()))
#	print mat1
	for i in np.arange(len(mat1)):
    	#	print float(lines[0].split()[i])
    		mat1[i] += float(lines[0].split()[i])
		
#        print mat1
	mat2 = np.zeros(len(lines[1].split()))
	for i in np.arange(len(mat2)):
    		mat2[i] += float(lines[1].split()[i])
#        print mat2
	maxx1=max(mat1)
	maxx2=max(mat2)

	mat3 = np.zeros(len(lines[2].split()))
#	print mat1
	for i in np.arange(len(mat3)):
    	#	print float(lines[0].split()[i])
    		mat3[i] += float(lines[2].split()[i])
		
#        print mat1
	mat4 = np.zeros(len(lines[3].split()))
	for i in np.arange(len(mat4)):
    		mat4[i] += float(lines[3].split()[i])


	mat5 = np.zeros(len(lines[4].split()))
	for i in np.arange(len(mat5)):
    		mat5[i] += float(lines[4].split()[i])


	mat6 = np.zeros(len(lines[5].split()))
	for i in np.arange(len(mat6)):
    		mat6[i] += float(lines[5].split()[i])


	mat7 = np.zeros(len(lines[6].split()))
	for i in np.arange(len(mat7)):
    		mat7[i] += float(lines[6].split()[i])


	mat8 = np.zeros(len(lines[7].split()))
	for i in np.arange(len(mat8)):
    		mat8[i] += float(lines[7].split()[i])
#        print mat2
	#for i in np.arange(len(mat1)):
        #       print float(lines[0].split()[i])
        #        mat1[i] = mat1[i]/maxx1
	#	mat2[i] = mat2[i]/maxx2

#	print mat1
#	print mat2

#error_11= (0.011967031,	0.052035861,	0.015301899,	0.03786735,	0.046621448,	0.099768305,	0.010955834)
#error_1=(0.061151853,	0.098024924,	0.164472068,	0.093041836,	0.161066204,	0.089685768,	0.064119679)
#	error =  (0.3497,0.3108,1,1,1,1,1,1,0.45,0.89,0.89,0.1,0.24,0.24,0.45)
	ind = np.arange(len(mat1))  # the x locations for the groups
	width = 0.42       # the width of the bars
#	yt = (88888888)
#	print yt
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax2 = ax.twinx()
#	rects1 = ax.bar(ind, mat1, width, color='#4169E1', align='center', edgecolor='none', yerr=error, error_kw=error_config)
        #patterns = [ "."]
	#colors = cm.autumn
	rects1 = ax.bar(ind, mat1, width, color='#0072b2', align='center', edgecolor='none',yerr=mat3,error_kw=dict(lw=1, capsize=5, capthick=1,ecolor='black'))    #upper i #006a4e #006eb #cce2cb
#	rects2 = ax.bar(ind + width, mat2, width, color='#000080',align='center', edgecolor='none', yerr=error_1, error_kw=error_config)
	rects2 = ax.bar((ind + width+0.0025), mat2, width, color='#d55e00',align='center', edgecolor='none',yerr=mat4,error_kw=dict(lw=1, capsize=5, capthick=1,ecolor='black')) #lower #fc9c54 #000093 #c8e7f5 #ffd8be


#	rects3 = ax.bar((ind), mat5, width, color='#d55e00',align='center', edgecolor='none',yerr=mat7,error_kw=dict(lw=1, capsize=5, capthick=1,ecolor='black')) #lower #fc9c54 #000093 #c8e7f5 #ffd8be


#	rects4 = ax.bar((ind +width+0.0025), mat6, width, color='#d55e00',align='center', edgecolor='none',yerr=mat8,error_kw=dict(lw=1, capsize=5, capthick=1,ecolor='black')) #lower #fc9c54 #000093 #c8e7f5 #ffd8be
#	rects3 = ax2.plot(ind, mat5,color='#006ca8',linestyle=" ",linewidth=0.8, marker="o")

	rects3 = ax2.errorbar(ind, mat5,color='#006ca8',linestyle=" ",linewidth=0.3, marker="o", yerr=mat7, lw=1, capsize=5, capthick=1,ecolor='#006ca8')
	#rects1= ax.bar(ind, mat5, color='#006ca8',yerr=(34.4343307548013, 34.3233688221839, 31.9229765826022, 33.4860988363865, 28.7005967089324, 30.0195654663666, 35.666090265011))

	rects4 = ax2.errorbar(ind+width+0.0025, mat6, color='#b85100',linestyle=" ",linewidth=0.8, marker="o",yerr=mat8, lw=1, capsize=5, capthick=1,ecolor='#b85100')

	#rects2.set_hatch('O')
#	#4682B4
# '#1E90FF'
	#ax.set_ylabel(ylab)
	#ax.set_title(ttl)
	ax.set_ylim(0,1400000)
	ax2.set_ylim(0,50)
	ax.set_xticks(ind + width / 2)
        #ax.set_yticks(np.arange (0,1.4),0.1)
#	ax.set_yticklabel(fontsize=14)
#	ax.set_yticks(np.arange(0.2,1.55555),1.0)
	#ax.set_yticks(ticks)
	ax.set_xticklabels(('I', 'II', 'III', 'IV', 'V','VI','VII'))
	ax.set_yticklabels(('0', '0.2', '0.4', '0.6', '0.8','1.0','1.2','1.4'))
        ax.spines["bottom"].set_linewidth(2.5)	
        ax.spines["top"].set_linewidth(2.5)	
        ax.spines["left"].set_linewidth(2.5)	
        ax.spines["right"].set_linewidth(2.5)	
#	plt.errorbar(xrange(7), [1,2,3,4,5,6,7], yerr=[[0,0.313700538,0.094183538,0.128553045,0.026031239,0.195261924,0.135774285],[4,10,6,8,14]])
#	ax.legend((rects1[0], rects2[0]), ('Lower-leaflet', 'Upper-leaflet'))
#If your file is mannulay arranged to give you the upper line as upper leaflet, then chnage the axes legends accrdingly.
#	leg = legend()
#	leg.get_frame().set_edgecolor('none')
#	ax.legend(loc='upper centre',bbox_to_anchor=(0, 0, 1, 1),edgecolor='none')
#	ax.legend((rects1[0],rects2[0]),('Upper-leaflet','Lower-leaflet'), frameon='False')
#	ax.legend(rects1[0],['1'],loc=4)

#def save('C:/',fna, ext='png', close=True, verbose=True):

#	ax.legend(loc=3 ,ncol=2, mode="expand", borderaxespad=0.)
#	l = legend(bbox_to_anchor=(0, 0, 1, 1), bbox_transform=gcf().transFigure)
	plt.xticks(fontsize=15,rotation=0)
	plt.yticks(fontsize=16)
#	ax.set_yticklabel(font='helevtica',fontsize=14)

	ax.tick_params(axis='y', which='major', width=3, length=6, top=False, right=False, labelsize=18)
	ax.tick_params(axis='both', which='major', width=3, length=6, top=False, right=False)
	plt.savefig(fna, dpi=600, transparent='True',bbox_intches='tight')


