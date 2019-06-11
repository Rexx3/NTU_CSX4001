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


def main():

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    # sentences = word2vec.LineSentence('segphases_{0}.txt'.format(args.novel_root))
    words = phase_seg(args.novel_root, "user_dict_{0}".format(args.dict))
    model = word2vec.Word2Vec(words, size=400, alpha=0.001,min_alpha=0.00001, min_count=20, iter=50)
    model.save("word2vec_{0}.model".format(args.dict))
def test():
    model = word2vec.Word2Vec.load("/Users/rex/data_science/models/word2vec_{0}.model".format(1))
    phase = input("Please input a phase: ")
    out = model.similar_by_vector(phase,topn=args.topn)
    word = []
    # for i in range(args.topn):
    #     word.append(" ".join(out[i][0]))
    try :
        os.path.isfile('tags.txt')
    except :
        open('tags.txt','w')
    f = open('tags.txt', 'w')
    for i in range(args.topn):
        f.write(out[i][0]+" ")
        print(out[i][0])
    f.close()
    # phase2 = input("Please input another phase")
    # print(model.similarity(phase, phase2))
    # X = model[model.wv.vocab]
    # pca = PCA(n_components=2)
    # result = pca.fit_transform(X)

    # pyplot.scatter(result[:, 0], result[:, 1])
    # words = list(model.wv.vocab)
    # for i, word in enumerate(words):
    #     pyplot.annotate(word.encode('utf-8'), xy=(result[i, 0], result[i, 1]))
    # pyplot.show()

    # 讀取每首歌的前10個tags

    text = open('tags.txt').read()
    print(text)
    # 設定停用字(排除常用詞、無法代表特殊意義的字詞)
    # stopwords = {}.fromkeys(["書"])
    # 產生文字雲
    wc = WordCloud(font_path="NotoSerifCJKtc-Black.otf", #設置字體
               background_color="white", #背景顏色
               max_words = 2000 ,)      #停用字詞
    wc.generate(text)
    # 視覺化呈現
    plt.imshow(wc)
    plt.axis("off")
    # plt.figure(figsize=(10,6), dpi = 100)
    plt.show()

def cha_names(dict):
    f = open(dict,'r')
    lines = f.readlines()
    names = []
    for line in lines:
        names.append(line.split(' ')[0])
    return names

def topnsim(list1,list2,model):
    count = 0
    for i in list1:
        for j in list2:
            count += model.similarity(i,j)
    return(count/(len(list1)*len(list2)))

def matrix():
    model = word2vec.Word2Vec.load('word2vec_{0}.model'.format(args.dict))
    names = cha_names("user_dict_{0}".format(args.dict))
    mat = np.zeros([len(names),len(names)])
    simphases = []
    for name in names:
        print(model.similar_by_vector(name,topn=args.topn))
        simphases.append([out[0] for out in model.similar_by_vector(name,topn=args.topn)])
    for i in range(len(names)):
        for j in range(len(names)):
            if i<=j:
                continue
            else:
                mat[i,j]=topnsim(simphases[i],simphases[j],model)
                mat[j,i]=topnsim(simphases[i],simphases[j],model)
    savepath = 'matrix_{}.csv'.format(args.dict)
    try:
        os.path.isfile(savepath)
    except:
        open(savepath,'w')
    f = open(savepath,'w',encoding = 'utf-8-sig')
    # writer = csv.writer(f)
    # writer.writerows("".names)
    np.savetxt(savepath,mat,delimiter=',')
    f.close()
    print(mat)




if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--dict", default=1, type=int)
    parser.add_argument("-n", "--novel_root", default='suck',type=str)
    parser.add_argument("-m", "--mode", default='train', type=str)
    parser.add_argument("-t", "--topn", default=10, type=int)
    args = parser.parse_args()
    if args.mode=='train':
        main()
    elif args.mode=='test':
        test()
    elif args.mode=='matrix':
        matrix()
