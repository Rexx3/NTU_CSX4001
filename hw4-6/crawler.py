# -*- coding: utf-8 -*
import requests
from bs4 import BeautifulSoup
import types
r = requests.get("https://8book.com/books/novelbook_102963.html")

soup = BeautifulSoup(r.text, "html.parser")
# print(soup.prettify())
link = []
for table in soup.find_all("table", {'class' : 'episodelist'}):
    for tr in table.find_all('tr'):
        for a in tr.find_all('a', href=True):
            link.append('https://8book.com/' + a['href'])
print(link)
# link = ["https://8book.com/readbook/3/104043/271586.html", "https://8book.com/readbook/3/104043/271587.html"]
novel=''
for i in range(len(link)):
    r = requests.get(link[i])
    r.encoding = 'big5'
    soup = BeautifulSoup(r.text, "html.parser")
    st = soup.find('p').stripped_strings
    for s in st:
        novel+=s.replace('(adsbygoogle = window.adsbygoogle || []).push({});', '')
f = open('novel_2.txt','w')
f.write(novel.encode('utf-8'))
f.close
    # p = soup.select("p", {'class' : 'content'})
    # print(p.text)
    #     for text in p.find_next_siblings('br'):
    #         print(text)

#     for elem in p.recursiveChildGenerator():
#         if isinstance(elem, types.StringTypes):
#             text += elem
#     print(text)
#     novel += text

