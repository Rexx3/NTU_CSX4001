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
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from matplotlib.font_manager import FontProperties
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
    mat = np.ones([len(names),len(names)])
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
    return names, mat

def plot_confusion_matrix(cm, classes, title=None, cmap=plt.cm.Blues):
    # if not title:
    #     if normalize:
    #         title = 'Normalized confusion matrix'
    #     else:
    #         title = 'Confusion matrix, without normalization'



    # classes = classes[unique_labels(y_true, y_pred)]
    # if normalize:
    #     cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    #     print("Normalized confusion matrix")
    # else:
    #     print('Confusion matrix, without normalization')
    cm = (cm-cm.min()) / (cm.max()-cm.min())
    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    myfont = FontProperties(fname=r'/Users/rex/Downloads/NotoSerifCJKtc-hinted/NotoSerifCJKtc-Black.otf')
    ax.set_xticklabels(classes, fontproperties=myfont)
    ax.set_yticklabels(classes, fontproperties=myfont)
    ax.set_title(title,fontproperties=myfont)
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),)
           # ... and label them with the respective list entries
           # xticklabels=classes, yticklabels=classes,
           # title=title,)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    # fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], '.2f'),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax

def main():
    np.set_printoptions(precision=2)
    class_names, cm = matrix()
    # Plot non-normalized confusion matrix
    plot_confusion_matrix(cm, classes=class_names,
                          title='獵命師角色相似度矩陣')

    # Plot normalized confusion matrix
    # plot_confusion_matrix(y_test, y_pred, classes=class_names, normalize=True,
    #                       title='Normalized confusion matrix')

    plt.show()

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--dict", default=1, type=int)
    parser.add_argument("-n", "--novel_root", default='suck',type=str)
    parser.add_argument("-m", "--mode", default='train', type=str)
    parser.add_argument("-t", "--topn", default=10, type=int)
    args = parser.parse_args()
    if args.mode=='train':
        main()
    # elif args.mode=='test':
    #     test()
    # elif args.mode=='matrix':
    #     matrix()