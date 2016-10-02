import os, glob
import re
script_dir= os.path.dirname(os.path.realpath('__file__'))
path =  os.path.join(script_dir[0:-3],'wx_data')
path1= os.path.join(script_dir[0:-3],'answers/YearlyAverages.out')
currentFile = glob.glob( os.path.join(path, '*.txt'))
currentFile.sort()
outputfile=open(path1,'w')
for files in currentFile:
	file = open(files,'r')
	lines = file.read().splitlines()
	row_sets = [[c for c in line.split()] for line in lines] # read and split the lines in the columns
	res=[]
	for year in range(1985,2015):
		subset = [row for row in row_sets if row[0][0:4] == str(year)]
		res.append(subset)
	no_of_lines = 0
	for rs in res:
		if rs:
			maxavg=0.00
			minavg=0.00
			pretotal=0.00
			year = ''
			for r in rs:
				year = r[0][0:4]
				maxavg+=float(r[1])
				minavg+=float(r[2])
				pretotal+=float(r[3])
				no_of_lines+=1
			if no_of_lines !=0:
				max_avg=format(maxavg/no_of_lines, '.2f')
				min_avg=format(minavg/no_of_lines,'.2f')
				total=format(pretotal, '.2f')
			else:
				max_avg=0.00
				min_avg=0.00
				total=0.00
			outputfile.write(files.split('/')[-1]+'\t'+year+'\t'+str(max_avg)+'\t'+str(min_avg)+'\t'+str(total)+'\n')

