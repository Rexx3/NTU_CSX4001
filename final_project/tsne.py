# -*- coding: utf-8 -*
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
from sklearn import manifold

def cha_names(dict):
    f = open(dict,'r')
    lines = f.readlines()
    names = []
    for line in lines:
        names.append(line.split(' ')[0])
    return names



def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    names = cha_names("user_dict_{0}".format(5))
    y = []
    yn = []
    name_vec = []
    for i in range(19):
        model = word2vec.Word2Vec.load("/Users/rex/data_science/models/word2vec_{0}.model".format(i+1))
        # lines = phase_seg(args.novel_root.format(i+1), "user_dict_{0}".format(args.dict))
        # freq = {}
        # for name in names:
        #     freq[name]=0
        # for words in lines:
        #     for word in words:
        #         if word in names:
        #             freq[word] +=1
        for name in names:
            # if freq[name]>40:
            try:
                name_vec.append(model[name])
                yn.append(name)
                y.append(names.index(name))
            except KeyError:
                print(name+" is not in model_{}...".format(i))
    tsne = manifold.TSNE(n_components=2, init='pca', random_state=501,perplexity=20,learning_rate=50)
    X_tsne = tsne.fit_transform(np.asarray(name_vec))

    print("Org data dimension is {}. Embedded data dimension is {}".format(np.asarray(name_vec).shape[-1], X_tsne.shape[-1]))

    '''嵌入空间可视化'''
    x_min, x_max = X_tsne.min(0), X_tsne.max(0)
    X_norm = (X_tsne - x_min) / (x_max - x_min)  # 归一化
    print(X_norm)
    # plt.rcParams['font.sans-serif'] = ['fuck'] 
    myfont = FontProperties(fname=r'/Users/rex/Downloads/NotoSerifCJKtc-hinted/NotoSerifCJKtc-Black.otf')
    plt.figure(figsize=(8, 8))
    for i in range(X_norm.shape[0]):
        plt.text(X_norm[i, 0], X_norm[i, 1], str(yn[i]), color=plt.cm.Set1(y[i]), fontproperties=myfont,
                 fontdict={'weight': 'bold', 'size': 9})
    plt.title('所有角色的向量關係',fontproperties=myfont)
    plt.xticks([])
    plt.yticks([])
    plt.show()



if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--dict", default=5, type=int)
    parser.add_argument("-n", "--novel_root", default='suck',type=str)
    parser.add_argument("-m", "--mode", default='train', type=str)
    parser.add_argument("-t", "--topn", default=10, type=int)
    args = parser.parse_args()
    if args.mode=='train':
        main()