import glob,os,re
from django.http import HttpResponse
import os.path
script_dir= os.path.dirname(os.path.realpath('__file__'))
path1 = os.path.join(script_dir[0:-3],'answers/MissingPrcpData.out')
path = os.path.join(script_dir[0:-3],'wx_data')
currentFile = glob.glob( os.path.join(path, '*.txt'))
currentFile.sort(key=lambda f: int(filter(str.isdigit, f)))
openfile1 = open(path1, 'w') 
for file in currentFile:
    x=file.split('/')[-1]
    with open(file,'rb') as openfile:
        lines = openfile.read().splitlines()
        row_sets = [[c for c in line.split()] for line in lines]
        count=0
        for row in row_sets:
            if row[3] == '-9999':
                count+=1
        openfile1.write(x.strip()+'\t'+str(count)+'\n')