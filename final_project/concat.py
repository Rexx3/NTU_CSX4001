# -*- coding: utf-8 -*
import os

path = '/Users/rex/data_science/novels/獵命師/'

filenames = os.listdir(path)
print(filenames)
savepath = '/Users/rex/data_science/novels/'
novel = 'novels/novel_all.txt'
try:
    os.path.isfile(novel)
except:
    open(novel,'w')
f = open(novel,'w')
for name in filenames:
    file = open(os.path.join(path,name),'r')
    lines = file.readlines()
    for l in lines:
        f.write(l)
f.close()
