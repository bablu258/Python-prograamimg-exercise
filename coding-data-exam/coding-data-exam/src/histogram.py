import numpy as np
import matplotlib.pyplot as plt

import os, glob
script_dir= os.path.dirname(os.path.realpath('__file__'))
path =  os.path.join(script_dir[0:-3],'wx_data')
file = open(script_dir[0:-3]+'answers/YearHistogram.out','r')
lines = file.read().splitlines()
row_sets = [[c for c in line.split()] for line in lines]
alphab = []
frequencies = []
for row in row_sets:
	alphab.append(str(row[0]))
	frequencies.append(int(row[1]))
pos = np.arange(len(alphab))
width = 1.0     # gives histogram aspect to the bar diagram

ax = plt.axes()
ax.set_xticks(pos + (width / 2))
ax.set_xticklabels(alphab)

plt.bar(pos, frequencies, width, color='r')
plt.show()