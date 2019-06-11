# -*- coding: utf-8 -*
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
f = open('/Users/rex/data_science/novels/愛情兩好三壞.txt')
lines = f.readlines()
path = '/Users/rex/data_science/novels/愛情兩好三壞_.txt'
try:
    os.path.isfile(path)
except:
    open(path,'w')
f = open(path,'w')
for l in lines:
    print(type(l))
    f.write(l)
f.colse()