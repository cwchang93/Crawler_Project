from selenium import webdriver
from bs4 import BeautifulSoup

web = webdriver.Chrome()
#num = 2614
#for
web.get("https://www.ptt.cc/bbs/Beauty/index+"+num+".html")
#index 換頁

html = web.page_source

soup = BeautifulSoup(html, "html.parser")
container = soup.select('.r-ent')

count = 1
#while count <=10:
for each in container:
    if count <= 100:
        title = each.select('div.title')[0].text.strip('\n')
    #print(type(title))
        author = each.select('div.author')[0].text
        date = each.select('div.date')[0].text
        allinfo = {'NO.':count,'標題':title, '作者':author, '日期':date}
        print(allinfo)
        print('count: ',count)
        count += 1

web.close()
