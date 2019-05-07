# coding=utf-8
import jieba 
import codecs
import os
from argparse import ArgumentParser
def main():
    f = codecs.open('novel_{0}.txt'.format(args.novel), 'r', 'utf-8')
    textseg=[]
    text = ''
    jieba.load_userdict("user_dict_{0}".format(args.novel))
    seg = jieba.cut(f.readlines()[0],cut_all=False)
    for s in seg:
        textseg.append(s)
    fileseg ='segphases_{0}.txt'.format(args.novel)
    try:
        os.path.isfile(fileseg)
    except:
        open(fileseg,'w')
    with open(fileseg,'w') as fW:
        for i in range(len(textseg)):
            fW.write(textseg[i].encode('utf-8'))
            fW.write('\n'.encode('utf-8'))

if __name__=='__main__':
    parser = ArgumentParser()
    parser.add_argument("-n", "--novel", default=1, type=int)
    args = parser.parse_args()
    main()


