# -*- coding: utf-8 -*
import requests
from bs4 import BeautifulSoup
import types
from argparse import ArgumentParser

def rootlinks(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")
    content = soup.find('div',{'class':'content'})
    for a in content.find_all('a', href=True):
        if 'liemingshichuanqi_' in str(a['href']):
            yield('http://big5.quanben5.com' + a['href'] + 'xiaoshuo.html')

def crawl(link):
    soup = BeautifulSoup(link, "html.parser")


def main():
    links = rootlinks(args.root)
    for idx,l in enumerate(links):
        sublink =[]
        print(l)
        r = requests.get(l)
        soup = BeautifulSoup(r.text, "html.parser")
        for tr in soup.find_all('li', {'class' : 'c3'}):
            for a in tr.find_all('a', href=True):
                sublink.append('http://big5.quanben5.com' + a['href'])
        print(sublink)
        # link = ["https://8book.com/readbook/3/104043/271586.html", "https://8book.com/readbook/3/104043/271587.html"]
        novel=''
        for i in range(len(sublink)):
            r = requests.get(sublink[i])
            r.encoding = 'utf-8'
            soup = BeautifulSoup(r.text, "html.parser")
            content = soup.find('div', {'id' : 'content'})
            for st in content.find_all('p'):#.stripped_strings:
                for s in st:
                    novel+=s.string#.replace('(adsbygoogle = window.adsbygoogle || []).push({});', '')
        f = open(args.novel.format(idx+10),'w')
        f.write(novel.encode('utf-8'))
        f.close


if __name__=='__main__':
    parser = ArgumentParser()
    parser.add_argument("-n", "--novel", default='/Users/rex/data_science/novels/novel{}.txt',type=str)
    parser.add_argument("-l", "--link", default='suck', type=str)
    parser.add_argument("-r", "--root", default='suck', type=str)
    parser.add_argument("-e", "--elink", default=False, type=bool)
    args = parser.parse_args()
    main()
