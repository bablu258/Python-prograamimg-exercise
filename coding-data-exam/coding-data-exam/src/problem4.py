import os, glob
import re
import scipy
from scipy.stats import pearsonr
script_dir= os.path.dirname(os.path.realpath('__file__'))
path =  os.path.join(script_dir[0:-3],'wx_data')
path1= os.path.join(script_dir[0:-3],'answers/Correlations.out')
totalfiles=os.listdir(path)
totalfiles.sort()
file = open(script_dir[0:-3]+'answers/YearlyAverages.out','r')
lines = file.read().splitlines()
outputfile=open(path1,'w')
row_sets = [[c for c in line.split()] for line in lines] # read and split the lines in the columns
res=[]
for fl in totalfiles:
    subset = [row for row in row_sets if row[0] == str(fl)]
    res.append(subset)
for rs in res:
    if rs:
        no_of_lines = 0
        l=[]
        m=[]
        n=[]
        filename=''
        for r in rs:
            l.append(float(r[2]))
            m.append(float(r[3]))
            n.append(float(r[4]))
            filename=r[0]
            no_of_lines+=1
        x = scipy.array(l)
        y = scipy.array(m)
        z = scipy.array(n)
        #correlation between max temperature and min temperature
        xy_correlation = pearsonr(x, y)
        #correlation between min temperature and precipitation
        yz_correlation = pearsonr(y, z)
        #correlation between max temperature and precipitation
        xz_correlation = pearsonr(x, z)
        outputfile.write(filename+'\t'+str(format(xy_correlation[0],'.2f'))+'\t'+str(format(yz_correlation[0],'.2f'))+'\t'+str(format(xz_correlation[0],'.2f'))+'\n')

