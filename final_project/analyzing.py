# coding=utf-8
from gensim.models import word2vec
import jieba
import logging
from argparse import ArgumentParser
from sklearn.decomposition import PCA
from matplotlib import pyplot
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from phase_segment import phase_seg
import csv
from matplotlib.font_manager import FontProperties
def cha_names(dict):
    f = open(dict,'r')
    lines = f.readlines()
    names = []
    for line in lines:
        names.append(line.split(' ')[0])
    return names

def plotData(plt, data, label):
    x = [p[0] for p in data]
    y = [p[1] for p in data]
    return(plt.plot(x, y, label = label))

def wordcloud(text):
    wc = WordCloud(font_path="NotoSerifCJKtc-Black.otf", #設置字體
               background_color="white", #背景顏色
               max_words = 2000 ,)      #停用字詞
    wc.generate_from_frequencies(text)
    # 視覺化呈現
    plt.imshow(wc)
    plt.axis("off")
    # plt.figure(figsize=(10,6), dpi = 100)
    plt.show()

def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    names = cha_names("user_dict_{0}".format(args.dict))
    datas = []
    target = [1,2,9,10,18,19]

    for i in range(1,20):
        lines = phase_seg(args.novel_root.format(i), "user_dict_{0}".format(args.dict))
        if i in target:
            freq = {}
            for name in names:
                freq[name]=0
            for words in lines:
                for word in words:
                    if word in names:
                        freq[word] +=1
    # wordcloud(freq)
            datas.append([((names.index(name)+1)*5,freq[name]) for name in names])
        if i ==19:
            f = open('mycsvfile.csv','w',encoding = 'utf-8-sig')
            w = csv.DictWriter(f,fieldnames = names)
            w.writeheader()
            w.writerow(freq)
            f.close()
    print(datas)
    p=[]
    fig , ax = plt.subplots()
    labels=['one','two','eight','nine','eighteen','nineteen']
    for data in datas:
        p.append(plotData(plt,data,labels[datas.index(data)]))
        plt.legend()
    print(p)
    myfont = FontProperties(fname=r'/Users/rex/Downloads/NotoSerifCJKtc-hinted/NotoSerifCJKtc-Black.otf')
    # plt.legend(handles=p,labels=['one','two','eight','nine','eighteen','nineteen'], loc='upper left')
    plt.title('各角色在特定卷數所出現的頻率', fontproperties=myfont)
    plt.xticks(range(5,125,5),names,fontproperties=myfont)
    ax.legend()
    plt.show()
    #     # model = word2vec.Word2Vec(words, size=400, alpha=0.001,min_alpha=0.00001, min_count=5, iter=50)
    #     # model.save("/Users/rex/data_science/models/word2vec_{0}.model".format(i))



if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--dict", default=5, type=int)
    parser.add_argument("-n", "--novel_root", default='suck',type=str)
    parser.add_argument("-m", "--mode", default='train', type=str)
    parser.add_argument("-t", "--topn", default=10, type=int)
    args = parser.parse_args()
    if args.mode=='train':
        main()