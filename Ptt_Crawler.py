import os
import requests
import re
from bs4 import BeautifulSoup

nameOfBoard = input('please input name of board: ')    # ex: NBA
numbersOfArticles = int(input('please input numbers of the crawling articles: '))    # ex: 20
url = 'https://www.ptt.cc/bbs/' + nameOfBoard + '/index.html'

resp = requests.get(url)    # Send our request and get the respondence
resp.encoding = 'utf-8'    # To encode Chinese
# print(resp.text)    # HTML structure
soup = BeautifulSoup(resp.text, 'lxml')    # Use lxml of BeautifulSoup as parser to parse the HTML structure
# print(soup)    # after parser

a = soup.find_all('a', attrs={'class': 'btn wide'})    # Locate index by a-label  (<a class="btn wide" href="/bbs/NBA/index6181.html">‹ 上頁</a>)
print(a)

# Access the value of the href-attribute by attrs method
# att = a[1]
# print(att.attrs['href'])
# Access the value of the href-attribute by dict's key
# print(a[1]['href'])

str1 = a[1]['href']
# print('str1: ', str1)

pat1 = 'index\d+'

str2 = re.findall(pat1,str1)    # Locate the indexxxxx by re
# print('str2: ', str2)
pat2 = '\d+'

index = re.findall(pat2,str2[0])    # Locate the index of PTT NBA second page from indexxxxx
# print('index: ', index)

index = int(index[0]) + 1    # The index of last page

# print(index)
count = 0    # Count the numbers of saved articles
while True:
    urlpath = 'https://www.ptt.cc/bbs/' + nameOfBoard + '/index' + str(index) + '.html'    # Url of the page of the board, and the index will decrease by 1 after each loop
    _resp = requests.get(urlpath)    # Send our request and get the respondence
    _resp.encoding = 'utf-8'    # To encode Chinese
    _soup = BeautifulSoup(_resp.text, 'lxml')    # Parse
#     print('_soup: ', _soup)
    titleList = _soup.find_all('div', attrs={'class': 'title'})
    authorList = _soup.find_all('div', attrs={'class': 'author'})
    dateList = _soup.find_all('div', attrs={'class': 'date'})
#     print(titleList)
    titleList.reverse()
    for ind, val in enumerate(titleList):
        if count >= numbersOfArticles:
            break
        if not val.find_all('a'):
            continue    # if(本文已被刪除), go to next loop
        urlOfArticle = 'https://www.ptt.cc' + val.find('a')['href']    # /bbs/NBA/M.1534386408.A.36B.html
        article_resp = requests.get(urlOfArticle)    # Send our request and get the respondence
        article_resp.encoding = 'utf-8'    # To encode Chinese
        article_soup = BeautifulSoup(article_resp.text, 'lxml')
#         print(article_soup)
        content = article_soup.find('div', attrs={'id': 'main-content'})

        print('count = ', count)
        print('url of article: ', urlOfArticle)
        article_resp = requests.get(urlOfArticle)
        article_resp.encoding = 'utf-8'
        article_soup = BeautifulSoup(article_resp.text, 'lxml')
#         print(article_soup)
        author = authorList[ind].text
        print('author: ', author)
        date = dateList[ind].text
        print('date: ', date)
        title = titleList[ind].text
        print('title: ', title)
        print('content: ', content.text)
        print('===============================================================================================')
        print('=======================================     我是分隔線    =======================================')
        print('===============================================================================================')
        count += 1
    if count >= numbersOfArticles:
        break
    index -= 1

    
