
#------->>>>>URL协议一般格式：protocol://hostname[port]/path/[;parametres][?query]#fragment
#                             协议      主机名[端口]   路径      参数        查询     片段

#------->>>>>URL协议一般格式：scheme://netloc/path;parametres?query#fragment
#                             协议    域名   路径      参数   查询条件  锚点



import urllib.request as urt
from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
import urllib.parse as urp
import urllib.error as ure
from urllib.error import URLError
from urllib.robotparser import RobotFileParser
import http.cookiejar
import requests

from bs4 import BeautifulSoup


import json
import time
import socket
import re



# response = urt.urlopen('https://www.python.org')

# 获取响应类型
# print(type(response))

# 获取对象方法
# print(dir(response))

# 查看对象属性
# print(response.__dict__)

# 调用对象的属性
# print(response.version)

# 调用对象的方法
# html = response.read()

# 响应头的信息
# print(response.getheaders())

# print(response.getheader('Content-Type'))

# print(html.decode('utf-8'))


'''''
# urlopen中data参数的作用,urlopen()函数不支持验证、cookie或其他HTTP高级功能

data = bytes(urp.urlencode({'name':'cghr'}),encoding='utf-8')

response = urt.urlopen('http://httpbin.org/post',data = data)

html = response.read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())


'''''

'''''


# urlopen中timeout参数的作用,爬取过程中设置超时跳过爬取数据

try:
    response = urt.urlopen('http://httpbin.org/post',timeout=0.1)          #检测范围

except ure.URLError as e:           # ure.URLError可以将所有的异常包括在内；将异常赋予变量e
    if isinstance(e.reason,socket.timeout):
        print('Time Out')


'''''




'''''

request = urt.Request('https://www.python.org')
response = urt.urlopen(request)
html = response.read().decode('utf-8')
soup = BeautifulSoup(html,'html.parser')
print(soup.prettify())

'''''


'''''


# urllib.request中Request方法的作用


url = 'http://httpbin.org/post'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Host':'httpbin.org'
}        # headers也可以用get_header()添加
dic = {
    'name':'cghr'
}
data = bytes(urp.urlencode(dic),encoding='utf-8')
request = urt.Request(url = url,data = data,headers = headers,method='POST')
response = urt.urlopen(request)
html = response.read().decode('utf-8')

soup = BeautifulSoup(html,'html.parser')
print(soup.prettify())


'''''


'''''

#   HTTPBasicAuthHandler处理器（Web客户端授权验证）

username = 'chen8334912'
password = 'chenliang8334912'
url = 'https://chen8334912.cn9.quickconnect.cn'

# 构建一个密码管理对象，用来保存需要处理的代理服务器、用户名和密码等等
p = urt.HTTPPasswordMgrWithDefaultRealm()

# 添加账户信息，第一个参数realm是与远程服务器相关的域信息，一般没人管它都是写None，后面三个参数分别是 代理服务器、用户名、密码
p.add_password(None,url,username,password)

# 3. 构建一个HTTP基础用户名/密码验证的HTTPBasicAuthHandler处理器对象，参数是创建的密码管理对象
auth_handler = urt.HTTPBasicAuthHandler(p)

# 设置代理服务器
proxy_handle= urt.ProxyHandler({
                            'http':'123.56.74.221:80',
                            'https':'123.56.74.221:80'
})

# 通过 build_opener()方法使用这些代理Handler对象，创建自定义opener对象，参数包括构建的 auth_handler和代理IP
opener = urt.build_opener(auth_handler,proxy_handle)

try:
    # 调用自定义opener对象的open()方法,发送请求
    result = opener.open(url)
    html = result.read().decode('utf-8')
    soup = BeautifulSoup(html,'html.parser')
    print(soup.prettify())
except URLError as e:
    print(e.reason)


'''''


'''''


#---->>>>获取Cookie，并保存到CookieJar()对象中
#---->>>>CookieJar：管理HTTP cookie值、存储HTTP请求生成的cookie、向传出的HTTP请求添加cookie的对象。整个cookie都存储在内存中，对CookieJar实例进行垃圾回收后cookie也将丢失。



# 构建一个CookieJar对象实例来保存cookie
cookiejar = http.cookiejar.CookieJar()

# 使用HTTPCookieProcessor()来创建cookie处理器对象（构建一个handler），参数为CookieJar()对象
handler = urt.HTTPCookieProcessor(cookiejar)

# 通过 build_opener() 来构建opener
opener = build_opener(handler)

# 4. 以get方法访问页面，访问之后会自动保存cookie到cookiejar中
opener.open('http://www.baidu.com')

## 可以按标准格式将保存的Cookie打印出来
cookieStr = ''
for item in cookiejar:
    # print(item.name + "=" + item.value)
    cookieStr = cookieStr + item.name + "=" + item.value + ";"

# 舍去最后一位的分号
# print(cookieStr[:-1])

'''''


'''''


#------->>>>>> 访问网站获得cookie，并把获得的cookie保存在cookie文件中

# 保存cookie的本地磁盘文件名
filename = 'cookie.txt'

# 声明一个MozillaCookieJar(有save实现)对象实例来保存cookie，之后写入文件
cookiejar = http.cookiejar.MozillaCookieJar(filename)

# 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
handler = urt.HTTPCookieProcessor(cookiejar)

# 通过 build_opener() 来构建opener
opener = urt.build_opener(handler)

# 创建一个请求，原理同urllib2的urlopen
response = opener.open('http://www.baidu.com')

# 保存cookie到本地文件
cookiejar.save(ignore_discard=True,ignore_expires=True)


'''''


'''''


#------->>>>>从文件中获取cookies，做为请求的一部分去访问



# 创建MozillaCookieJar(有load实现)实例对象
cookiejar = http.cookiejar.MozillaCookieJar()

# 从文件中读取cookie内容到变量
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)

# 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
handler = urt.HTTPCookieProcessor(cookiejar)

# 通过 build_opener() 来构建opener
opener = urt.build_opener(handler)
print(opener.read().decode('utf-8'))

'''''


'''''


# --------->>>>>>利用cookielib和post登录人人网


# 1. 构建一个CookieJar对象实例来保存cookie
cookie = http.cookiejar.CookieJar()

# 2. 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
cookie_handler = urt.HTTPCookieProcessor(cookie)

# 3. 通过 build_opener() 来构建opener
opener = urt.build_opener(cookie_handler)

# 4. addheaders 接受一个列表，里面每个元素都是一个headers信息的元祖, opener将附带headers信息
opener.addheaders = [('User-Agent',
                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36')]

# 5. 需要登录的账户和密码
data = {'email': 'mr_mao_hacker@163.com', 'password': 'alaxxxxxime'}

# 6. 通过urlencode()转码,将str类型转换为bytes类型
postdata = urp.urlencode(data).encode('utf-8')

# 7. 构建Request请求对象，包含需要发送的用户名和密码
request = urt.Request('http://www.renren.com/PLogin.do', data=postdata)

# 8. 通过opener发送这个请求，并获取登录后的Cookie值，
opener.open(request)

# 9. opener包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
response = opener.open('http://www.renren.com/410043129/profile')

# 10. 打印响应内容
print(response.read().decode('utf-8'))


'''''



'''''

#------------>>>>网页内容下载到本地


response = urt.urlopen('https://www.hao123.com')
html = response.read()
html = html.decode('utf-8')
with open('urllib_test.txt','w',encoding='utf-8') as f:
    f.write(str(html))
    f.close


print(html)


'''''

'''''
#------------>>>>取一张图片

response = urt.urlopen('https://tp-y.zdmimg.com/201907/18/5d3007e404e2f129.jpg_d480.jpg')

print(response.info())    # 返回HTTPMessage对象，表示远程服务器返回的头信息
print(response.getcode())    #返回Http状态码。如果是http请求，200请求成功完成;404网址未找到
print(response.geturl())    # 返回请求的url


'''''


'''''
#  等同于上面一句

req = urt.Request('https://tp-y.zdmimg.com/201907/18/5d3007e404e2f129.jpg_d480.jpg')    # 使用request包装请求
response = urt.urlopen(req)  # 通过urlopen获取页面



# xi_img = response.read()
# with open('taifeng.jpg','wb') as f:    # 二进制格式去操作
#     f.write(xi_img)


'''''



'''''

Remote Address: 220.181.76.83:80    # 服务器的ip地址和端口

Request URL: http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule    # 请求的链接地址

Request Method: POST    # 请求的方法，这里是post请求

Status Code: 200 OK    #相应正常


'''''

'''''

# POST请求的目标url
url = 'https://www.hao123.com'



#安装进默认环境
urt.install_opener(opener)

response = urt.urlopen(url)

html = response.read().decode('utf-8')
print(html)

'''''


'''''


# 有道云翻译



count = 5

while count:
    content = input('please input:')
    if content == 'chris':
        print('现在我们凉凉了')
    else:
        break

# POST请求的目标url
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom='


# 设置代理服务器
proxy_support = urt.ProxyHandler({'http':'123.56.74.221:80'})


# 创建一个包含代理ip的opener
opener = urt.build_opener(proxy_support)


#安装进默认环境
urt.install_opener(opener)



# 设置headers参数，伪装成浏览器访问，添加User-Agent，完善请求信息
headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
            'Origin':'http://fanyi.youdao.com/',
            'Referer':'http://fanyi.youdao.com/'
          }


# 将需要POST的内容，以字典的形式记录在data内
formdata= {
            'type':'AUTO',
            'i':content,          # 需翻译的内容
            'doctype':'json',
            'xmlversion':'2.1',
            'keyfrom':'fanyi.web',
            'ue':'utf-8',
            'action':'FY_BY_REALTlME',    # 判断当你是按回车提交或者点击按钮提交的方式
            'typoResult':'true'
            }

formdata = urp.urlencode(formdata).encode('utf-8')

#post需要输入两个参数，一个是刚才的链接，一个是formdata，返回的是一个Response对象
response = urt.urlopen(url,formdata)

# 在request对象生成之后，没用add_header()方法追加headers参数
#response.add_header('Referer','http://fanyi.youdao.com/')
#response.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')


html = response.read().decode('utf-8')
print(html)
target = json.loads(html)
print(target, type(target))
print(target['translateResult'][0][0]['tgt'])
time.sleep(3)      # 延缓提交时间

'''''



'''''


制作爬虫时需要注意的HTTP字段
HTTP请求头部分字段解释：

accept：表明请求的资源类型

accept-charset：表示请求的资源的编码方式

accept-encoding：表明发送方可以支持的编码方式，需要注意gzip，它表示的是压缩，服务器为了节省空间可能就会压缩资源，如果我们的http头部含有gzip，在爬虫中要记得用gzip解码。

connection：keep-alive：避免建立的TCP连接被关闭，当加载完所需要的全部资源后，会发送一个头部带有connection：close的http报文关闭TCP连接，因为爬虫不需要多次请求数据（例如加载网页时，获得了html文件后，还会请求获得css、js等文件），所以可以直接去掉，或者将值设置为close

cookie：一般的登陆策略是把登陆的信息写入cookie，服务器把cookie返回给客户端，客户端每次请求数据都会带上cookie，cookie中存储的数据一般比较小

 

 

HTTP响应头部分字段解释：

set—cookie：设置cookie

status：状态码，表明服务器响应请求的状态，状态码返回403，可能是需要登陆，或者是IP被封禁（如果是拨号上网（通过DHCP动态分配IP），一般等待十秒左右再次拨号即可分到不同的公网IP），状态码表示重定向时，在urllib2会自动对重定向做处理，如果状态码为5xx，不一定就是服务器宕机，在分布式爬虫中，如果爬取同一服务器的不同网页的多个爬虫连续收到5XX，则可能是服务器宕机

'''''

'''''

#  用python实现的BFS爬取豆瓣电影首页超链接



from urllib import request
from collections import deque
from pybloom_live import BloomFilter
from lxml import etree
import hashlib


class crawel_bfs:
    request_header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'bid=Kn9AT5duD7k; gr_user_id=32e433a7-19f0-4e17-80c4-56b58d7c0056; _vwo_uuid_v2=5985FEE132C29EC9C840D6C5EDD95323|67c2ccc8467fc02a9cce6928e86ea013; ll="118281"; __yadk_uid=I4Ki5RUaEWOUdpVIjJfRYo1MEuaW36hA; __utmv=30149280.16369; viewed="10483489_1115600_2230208_26857712_1569487_1623164_26708119_26677686"; __utma=30149280.965685249.1516632348.1528892392.1530880979.81; __utmc=30149280; __utmz=30149280.1530880979.81.57.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=30149280.1.10.1530880979; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1530880982%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.2038558801.1520348154.1528892435.1530880982.55; __utmb=223695111.0.10.1530880982; __utmc=223695111; __utmz=223695111.1530880982.55.51.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=da4243a2a9e242f1.1520348154.54.1530881042.1528892472.',
        'Host': 'movie.douban.com',
        'Referer': 'https://www.douban.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }

    cur_level = 0
    max_level = 2

    download_bf = BloomFilter(1024 * 1024, 0.01)

    childque = deque()
    nowque = deque()

    def __init__(self, url, file_md5name, file_urlname):
        self.file_urlNameMd5_name = file_md5name
        self.file_urlName_name = file_urlname
        self.deal_file_md5 = open(self.file_urlNameMd5_name, 'r')
        self.file_md5 = self.deal_file_md5.readlines()
        # 用于输入现有的文件
        for url_md5_name in self.file_md5:
            # -1表示的是换行符,读入时换行符不会占据两个字符
            self.download_bf.add(url_md5_name[:-1])
        self.deal_file_md5.close()
        self.file_md5 = open(self.file_urlNameMd5_name, 'a')
        self.file_url = open(self.file_urlName_name, 'a')
        self.nowque.append(url)

    def indeque(self, url):
        self.nowque.append(url)

    def outdeque(self):
        try:
            url = self.nowque.popleft()
            return url
        except Exception:
            self.cur_level += 1
            if self.cur_level == self.max_level:
                return None
            if len(self.childque) == 0:
                return None
            self.nowque = self.childque
            self.childque = deque()
            return self.nowque.popleft()

    def crawler(self, url):
        try:
            # 创建一个request对象，封装一个报文对象
            req = request.Request(url, headers=self.request_header)
            # 发送报文
            response = request.urlopen(req)
            html_page = response.read()
            # 按照固定编码解码
            html = etree.HTML(html_page.lower().decode('utf-8'))
            url_list = html.xpath('//a/@href')
            for url in url_list:
                if url.find('javascript:') != -1:
                    continue
                if url.startswith('http://') is False:
                    if url.startswith('/') is True:
                        url = 'http://movie.douban.com' + url
                    else:
                        continue
                if url[-1] == '/':
                    url = url[:-1]
                temp = hashlib.md5(url.encode('utf-8')).hexdigest()
                if temp not in self.download_bf:
                    self.download_bf.add(url)
                    self.childque.append(url)
                    self.file_md5.write(temp + '\n')
                    self.file_url.write(url + '\n')
        except Exception:
            print("出现异常")

    def startcrawler(self):
        while True:
            url = self.outdeque()
            if url != None:
                print("现在爬取" + url + "的超链接")
                self.crawler(url)
            else:
                break
        self.file_md5.close()
        self.file_url.close()


crawel = crawel_bfs("https://movie.douban.com/", 'urlmd5.txt',
                    'urlname.txt')
crawel.startcrawler()



'''''
'''''

# 自制翻译器

import requests
import json
from tkinter import Tk,Button,Entry,Label,Text,END

class YouDaoFanyi(object):
    def __init__(self):
        pass
    def crawl(self,word):
        url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        # 使用post需要一个链接
        data={
                'i': word,
                'from': 'AUTO',
                'to': 'AUTO',
                'smartresult': 'dict',
                'client': 'fanyideskweb',
                'doctype': 'json',
                'version': '2.1',
                'keyfrom': 'fanyi.web',
                'action': 'FY_BY_REALTIME',
                'typoResult': 'false'
                }
        # 将需要post的内容，以字典的形式记录在data内。
        r = requests.post(url, data)
        # post需要输入两个参数，一个是刚才的链接，一个是data，返回的是一个Response对象
        answer=json.loads(r.text)
        # 你可以自己尝试print一下r.text的内容，然后再阅读下面的代码。
        result = answer['translateResult'][0][0]['tgt']
        return result

class Application(object):
    def __init__(self):
        self.window = Tk()
        self.fanyi = YouDaoFanyi()
         
        self.window.title(u'我的翻译')
        # 设置窗口大小和位置
        self.window.geometry('310x370+500+300')
        self.window.minsize(310,370)
        self.window.maxsize(310,370)
        # 创建一个文本框
        #self.entry = Entry(self.window)
        #self.entry.place(x=10,y=10,width=200,height=25)
        #self.entry.bind("<Key-Return>",self.submit1)
        self.result_text1 = Text(self.window,background = 'azure')
        # 喜欢什么背景色就在这里面找哦，但是有色差，得多试试：http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
        self.result_text1.place(x = 10,y = 5,width = 285,height = 155)
        self.result_text1.bind("<Key-Return>",self.submit1)
        
        # 创建一个按钮
        # 为按钮添加事件
        self.submit_btn = Button(self.window,text=u'翻译',command=self.submit)
        self.submit_btn.place(x=205,y=165,width=35,height=25)
        self.submit_btn2 = Button(self.window,text=u'清空',command = self.clean)
        self.submit_btn2.place(x=250,y=165,width=35,height=25)
         
        # 翻译结果标题
        self.title_label = Label(self.window,text=u'翻译结果:')
        self.title_label.place(x=10,y=165)
        #翻译结果
         
        self.result_text = Text(self.window,background = 'light cyan')
        self.result_text.place(x = 10,y = 190,width = 285,height = 165)
        # 回车翻译
    def submit1(self,event):
        #从输入框获取用户输入的值
        content = self.result_text1.get(0.0,END).strip().replace("\n"," ")
        #把这个值传送给服务器进行翻译
        
        result = self.fanyi.crawl(content)
        #将结果显示在窗口中的文本框中
        
        self.result_text.delete(0.0,END)
    self.result_text.insert(END,result)

        #print(content)

    def submit(self):
        #从输入框获取用户输入的值
        content = self.result_text1.get(0.0,END).strip().replace("\n"," ")
        #把这个值传送给服务器进行翻译
        
        result = self.fanyi.crawl(content)
        # 将结果显示在窗口中的文本框中
        
        self.result_text.delete(0.0,END)
        self.result_text.insert(END,result)
        print(content)
        # 清空文本域中的内容
        def clean(self):
            self.result_text1.delete(0.0,END)
            self.result_text.delete(0.0,END)
        
        def run(self):
            self.window.mainloop()
 
if __name__=="__main__":
    app = Application()
    app.run()


'''''

# https://www.jb51.net/article/143229.htm



'''''



爬取网页的流程一般如下：

选着要爬的网址（url）
使用 python 登录上这个网址（urlopen、requests 等）
读取网页信息（read() 出来）
将读取的信息放入 BeautifulSoup
使用 BeautifulSoup 选取 tag 信息等


'''''


'''''

def main():
    url = 'http://baike.baidu.com/view/284853.htm'

    # 打开指定网址的html文件
    response = urt.urlopen(url)

    # 读取指定网址的html文件
    html = response.read().decode('utf-8')

    # 解析指定网址的html文件
    # BeautifulSoup：表示一个文档的全部内容。大部分时候，可以把它当作 Tag 对象，是一个特殊的 Tag
    # BeautifulSoup 主要用来遍历子节点及子节点的属性，并提供了很多方法，比如获取 子节点、父节点、兄弟节点等，但通过实践来看，这些方法用到的并不多。我们主要用到的是从文档树中搜索出我们的目标
    soup = BeautifulSoup(html, 'html.parser')

    # 标准的缩进格式的结构输出
    # print(soup.prettify())


    # 获取title标签                      获取title标签的文本内容
    print(soup.title, soup.title.name, soup.title.string)

    # find_all() 方法搜索当前 tag 的所有 tag 子节点，并判断是否符合过滤器的条件
    print(soup.find_all('b'))

    for each in soup.find_all(href = re.compile('view')):
        # print(each)
        # print(each.text)
        print(each.text, '------>', ''.join(['http://baike.baidu.com', each['href']]))


    
'''''



'''''

# 关键字查询，副标题+链接

def main():

    keyword = input('请输入查询关键词：')
    # 把关键字转码成%E8%83%A1%E6%AD%8C
    keyword = urp.urlencode({'word': keyword})
    # https://baike.baidu.com/search/word?word=%E8%83%A1%E6%AD%8C
    # 打开网页
    response = urt.urlopen('http://baike.baidu.com/search/word?%s' % keyword)
    # 获取网页输出
    html = response.read()
    # 使用beautifulsoup读取html
    soup = BeautifulSoup(html, 'html.parser')
    # 中文字符
    zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')

    # 开始第二遍的遍历
    for each in soup.find_all(href=re.compile('view')):
        # find_all 代表全文搜索，find 只会显示一条结果
        # href = re.compile("view") 如下例子
        # <a target=_blank href=/view/5458338.htm>一念执着</a>
        # re.compile('view') 正则匹配有view关键字的链接

        content = ''.join([each.text])
        # <a href="/wikicategory/view?categoryName=多肉植物" target="_blank">多肉百科<>
        # content = 多肉百科

        if content == "":
            continue
        # 如果标题为空则中止本次循环

        url2 = ''.join(['http://baike.baidu.com', each['href']])
        # 拼接新的URL
        # （http://baike.baidu.com）+ (/wikicategory/view?categoryName=多肉植物)
        # 出现了一个问题，有点链接是完整的，然后再加上前缀就不对了： http://baike.baidu.comhttp://baike.baidu.com/view/12878522.htm

        if zh_pattern.search(url2):
            continue
        # 如果url中包含中文则中止本次循环，因为编码不一样就会报错然后结束程序

        response2 = urt.urlopen(url2)
        html2 = response2.read()
        soup2 = BeautifulSoup(html2, 'html.parser')
        # 打开网址如下:
        # http://baike.baidu.com/view/482616.htm
        # 然后获取网页内容

        if soup2.h2:
            content = ''.join([content, soup2.h2.text])
        # 如果网页h2标签存在，则重新定义content
        # 光棍
        # 光棍(单身人士称谓)

        content = ''.join([content, "->", url2])
        print(content)
    # 最后打印完整的内容
    # 逍遥叹（胡歌演唱歌曲）->http://baike.baidu.com/view/345628.htm


if __name__ == '__main__':
    main()


'''''

'''''


import urllib.request
from bs4 import BeautifulSoup
import time

print("***\n***\n***\n这是一个爬虫，正在爬取百度贴吧的一个内容，请耐心等候：。。。")
f = open('nuc_pachong.txt', 'a+', encoding='utf-8')  # 打开文件,a+表示在文件末尾追加
end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 当前的时间
f.write("【时间：" + end_time + "】\n【标题】中北大学贴吧" + '\n')

url = "http://tieba.baidu.com/f?ie=utf-8&kw=%E4%B8%AD%E5%8C%97%E5%A4%A7%E5%AD%A6"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "lxml")
# print(soup.prettify())#打印格式
all = soup.find_all("a",
                    class_="j_th_tit ")  # 查找标签中的class_="zm-editable-content clearfix"，由于class在python中是保留变量名，所以class改写成class_;limit表示限制输出的数量
print(all)
ALL = str(all).split('</a>')
ALL.pop()  # 如果删除最后一元素“]”后面会报错

i = 0
for s in ALL:
    q, w = s.split('title="')
    i += 1
    f.write('【标题' + str(i) + '】：' + w + '\n')

f.close()
print("***\n***\n***\n恭喜你，已经完成任务，请你打开文件：nuc_pachong.txt查阅")

'''''



'''''

100：继续  客户端应当继续发送请求。客户端应当继续发送请求的剩余部分，或者如果请求已经完成，忽略这个响应。
101： 转换协议  在发送完这个响应最后的空行后，服务器将会切换到在Upgrade 消息头中定义的那些协议。只有在切换新的协议更有好处的时候才应该采取类似措施。
102：继续处理   由WebDAV（RFC 2518）扩展的状态码，代表处理将被继续执行。
200：请求成功      处理方式：获得响应的内容，进行处理
201：请求完成，结果是创建了新资源。新创建资源的URI可在响应的实体中得到    处理方式：爬虫中不会遇到
202：请求被接受，但处理尚未完成    处理方式：阻塞等待
204：服务器端已经实现了请求，但是没有返回新的信 息。如果客户是用户代理，则无须为此更新自身的文档视图。    处理方式：丢弃
300：该状态码不被HTTP/1.0的应用程序直接使用， 只是作为3XX类型回应的默认解释。存在多个可用的被请求资源。    处理方式：若程序中能够处理，则进行进一步处理，如果程序中不能处理，则丢弃
301：请求到的资源都会分配一个永久的URL，这样就可以在将来通过该URL来访问此资源    处理方式：重定向到分配的URL
302：请求到的资源在一个不同的URL处临时保存     处理方式：重定向到临时的URL
304：请求的资源未更新     处理方式：丢弃
400：非法请求     处理方式：丢弃
401：未授权     处理方式：丢弃
403：禁止     处理方式：丢弃
404：没有找到     处理方式：丢弃
500：服务器内部错误  服务器遇到了一个未曾预料的状况，导致了它无法完成对请求的处理。一般来说，这个问题都会在服务器端的源代码出现错误时出现。
501：服务器无法识别  服务器不支持当前请求所需要的某个功能。当服务器无法识别请求的方法，并且无法支持其对任何资源的请求。
502：错误网关  作为网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应。
503：服务出错   由于临时的服务器维护或者过载，服务器当前无法处理请求。这个状况是临时的，并且将在一段时间以后恢复。

'''''

'''''

#----->>>> error模块处理异常

# 因为URLError是HTTPError的父类，所以在捕获异常的时候可以先找子类是否异常，如果子类找不到，再找父类即可，先找子类中是否有HTTP错误，如果没有再找父类URL

request = urt.Request('https://cuiqingcai.com/index.htm')

try:
    response = urt.urlopen(request)

# err.code返回异常响应码，err.reason状态码错误原因，err.headers请求头

except ure.HTTPError as err:
    print(err,err.reason,err.code,err.headers,sep='\n')


# 返回错误原因,可以避免程序因为异常终止，同时异常得到有效的处理
except ure.URLError as err:
    print(err.reason,err)

else:
    print('good job')



'''''




'''''

#----->>>> parse模块解析链接



# urlparse

# result = urp.urlparse('https://www.baidu.com/s?tn=50000021_hao_pg&ie=utf-8&sc=UWd1pgw-pA7EnHc1FMfqnHRvPWm4n1TdnWc4riuW5y99U1Dznzu9m1YzrHbYnjcYP1b&ssl_sample=normal&srcqid=3415060727391552281&H123Tmp=nunew7&word=POST+data+should+be+bytes%2C+an+iterable+of+bytes%2C+or+a+file+object.+It+cannot+be+of+type+str.')
# print(result)
# print(type(result))
# print(result.scheme,result[0],result.netloc,result[1],sep='\n')





#urp.urlunparse,接受的参数是个可迭代对象，长度必须是6位

# data = ['https','taobao.com','index.html','user','a=6','comment']
# print(urp.urlunparse(data))


#urp.urljoin 链接拼接

# print(urp.urljoin('http://www.baidu.com','FAQ.html'))
# print(urp.urljoin('www.baidu.com','?FAQ.html'))



# urp.urlencode序列化为GET请求参数

params = {
    'name':'chris',
    'age':23
}
base_url = 'http://www.baidu.com'
new_url = base_url + urp.urlencode(params)
print(new_url)
query = 'name=chris&age=23'
print(urp.parse_qs(query),urp.parse_qsl(query))

'''''



'''''

#----->>>判断网页是否可以被爬取

rp= RobotFileParser()
rp.set_url('http://jianshu.com/robot.txt')
rp.read()
print(rp.can_fetch('*','http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*','https://www.baidu.com/s?wd=python3%20urlencoder&rsv_spt=1&rsv_iqid=0x8087feeb0033da14&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=50000049_hao_pg&rsv_enter=0&rsv_dl=tb&oq=python%2520urlencoder&rsv_t=6953VD29Ex1TfhF3nAOVUMiFofFHH031P7IZpujnf37ygyRbuiHEq%2FIbtVJytTbS4aKDZcJv&inputT=703&rsv_sug3=17&rsv_sug1=13&rsv_sug7=100&rsv_pq=b95dbca000004910&rsv_sug4=793'))

'''''

'''''


response = requests.get('https://httpbin.org/get')
#
# print(type(response))
# print(response.cookies)
print(response.text)
# print(type(response.text))


# 增加参数

data= {
    'name': 'chris',
    'age': 23
}
response2 = requests.get('https://httpbin.org/get',params=data)
print(response2.text)
print(response2.json())
print(type(response2.json()))



'''''




headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

response = requests.get('https://www.zhihu.com/explore',headers=headers).text

print(response)







# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
# titles = re.findall(pattern, response.text)
# print(titles)