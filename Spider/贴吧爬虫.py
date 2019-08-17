import urllib.request as urt
from bs4 import BeautifulSoup
import time


print('***\n***\n***\n this is a Spider , please waiting...')

f = open('Spider.txt','a+',encoding='utf-8')
end_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
f.write('[时间：'+end_time+']\n【标题】中北大学贴吧'+'\n')


url = 'http://tieba.baidu.com/f?ie=utf-8&kw=%E4%B8%AD%E5%8C%97%E5%A4%A7%E5%AD%A6'
html = urt.urlopen(url).read()

soup = BeautifulSoup(html,'lxml')

all = soup.find_all('a',class_='j_th_tit')
print(all)
ALL = str(all).split('<a>')
ALL.pop()



i = 0
for s in ALL:
    q,w = s.split('title=')
    i+=1
    f.write('[标题'+str(i)+']:'+w +'\n')

f.close()

print('Congratulations, it is over')



