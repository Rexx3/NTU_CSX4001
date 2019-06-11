# coding=utf-8
import jieba 
import codecs
import os
from argparse import ArgumentParser
def phase_seg(novel_root, dict):
    f = codecs.open(novel_root, 'r', 'utf-8')
    textseg=[]
    text = ''
    jieba.load_userdict(dict)
    lines = f.readlines()
    phases = []
    for line in lines:
        seg = jieba.cut(line,cut_all=False)
        phase = []
        for s in seg:
            phase.append(s)
        phases.append(phase)
    return phases
    # for s in seg:
    #     textseg.append(s)
    # fileseg ='segphases_{0}.txt'.format(args.novel)
    # try:
    #     os.path.isfile(fileseg)
    # except:
    #     open(fileseg,'w')
    # with open(fileseg,'w') as fW:
    #     for i in range(len(textseg)):
    #         fW.write(textseg[i].encode('utf-8'))
    #         fW.write('\n'.encode('utf-8'))

if __name__=='__main__':
    parser = ArgumentParser()
    parser.add_argument("-n", "--novel", default=1, type=int)
    args = parser.parse_args()
    main()


