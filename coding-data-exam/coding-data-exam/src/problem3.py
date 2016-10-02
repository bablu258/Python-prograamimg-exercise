import glob,os,re
import os.path
script_dir= os.path.dirname(os.path.realpath('__file__'))
path =  os.path.join(script_dir[0:-3],'answers/YearlyAverages.out')
path1= os.path.join(script_dir[0:-3],'answers/YearHistogram.out')
outputfile=open(path1,'w')
file = open(path,'r')
lines = file.read().splitlines()
row_sets = [[c for c in line.split()] for line in lines[1:]] # read and split the lines in the columns
res=[]
for year in range(1985,2015):
	subset = [row for row in row_sets if row[1] == str(year)]
	res.append(subset)
for rs in res:
	outputfile.write(rs[0][1]+'\t'+str(len(rs))+'\t'+str(len(rs))+'\t'+str(len(rs))+'\n')