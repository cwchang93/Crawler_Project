from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://www.chun-wei.com/")\
      .read().decode('utf-8')
#文字編碼可能是中文，因此decode('utf-8')

#print(html)
#最原始

soup = BeautifulSoup(html, features='lxml')
#print(soup.h1)
#print('\n', soup.p)

all_href = soup.find_all('a')
print(all_href)
all_href = [l['href'] for l in all_href]
#for i in all_href:
#    ls=[] 
#    ls += all_href['href']
#print(all_href)
