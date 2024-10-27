#!/usr/bin/env/python

import os
import re
from re import search
import sys
from matplotlib import pyplot as plt
import numpy as np

total=40001

filename = open("input.dat", "r")
#fn = open(fname, 'r')
lines = filename.readlines()
filename.close()
nsre = re.compile('([0-9]+)')
#print(lines)
#def sort_key(s):
#    return[int(text) if text.isdigit() else text.lower() for text in re.split(nsre,s )]

lines = [l.strip() for l in lines if not search('[~!@#$%^&*]', l)]
lines = np.array([l.split() for l in lines], dtype='float64')
data = np.zeros(len(lines))
data2 = np.zeros(3)
dimer = 0
monomer = 0
#    time = np.zeros(len(lines))
for i in np.arange(len(lines)-1):
    data[i] += float(lines[i])
    dimer += data[i]    

#print(data)
#print(dimer)

for i in np.arange(3):
    data2[i] += float(lines[i])
    
for i in np.arange(len(lines)):
    data[i] += float(lines[i])
    monomer = data[3]

#print(monomer)
data_two = [dimer, monomer]
all_dimers = (total - data[3])
#print(data_two)
#print(all_dimers)
print(data)
#all_data = [data2, monomer]
# Creating dataset
cars = ['True Dimers','Lipid mediated dimers','ICL3 dimers','all dimers']
#data = [1486,0,598517] #elastic-noel

colorsf = ( "midnightblue", "royalblue", "cornflowerblue", "darkred")
colorsd = ( "midnightblue", "royalblue", "cornflowerblue")
colorsb = ( "navy", "darkred")
# Creating plot
fig = plt.figure(figsize =(7, 7))
plt.pie(data,colors=colorsf)
plt.savefig("all.png",transparent=True,dpi=300)

#plt.pie(data_two,colors=colorsb)
#plt.savefig("both.png", transparent=True,dpi=300)

