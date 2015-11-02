
## bs4 로부터 BeatifulSoup 만 임포트.
from bs4 import BeautifulSoup

#html_doc = """
#<html><head><title>The Dormouse's story</title></head>
#<body>
#<p class="title"><b>The Dormouse's story</b></p>
#<p class="story">Once upon a time there were three little sisters; and their
#names were
#<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
#<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
#<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
#and they lived at the bottom of a well.</p>
#<p class="story">...</p>
#"""

## 파서 종류를 지정해줌. 디폴트가 html.parser
## 내가 원하느 파서가 잇으면 따로 지정 가능
#soup = BeautifulSoup(html_doc, "html.parser")
#print(soup.prettify()) # 예쁘게 출력.
#print(soup.a.prettify())


#print(soup.html.head.title) # title에 해당되는 태그 내용을 보여줌
#print(soup.title)
#soup.title.string # title을 string으로 변경
#print(soup.p) # 같은 이름의 태그가 여러개면 제일 먼저 나오는 것 알려줌

#print(soup.p['class']) # p 태그 안의 속성 값 가져오기

## p 태그를 가진것 전부 알려줌
#print("-----------------------------------")
#print(soup('a'))

## 해당되는 태그값을 가진 것만 반환?
#print("-----------------------------------")
#s1 = soup('a',{'id':'link1'})
#print(s1)
#s2=soup('p',{'class':'story'})
#print(s2)


## 계층구조속성 : 액세스한 것 기준으로 다시 액세스
#print("-----------------------------------")
#print(soup('a')[0].parent) # 부모자체
#soup('a')[0].parent.name # 부모의 이름
#soup('a')[0].contents # 자식
#soup('a')[0].NextSibling # 같은 위치 바로 앞
#soup('a')[0].previousSbling # 같은 위치 바로 뒤
#soup('a')[0].Next # 계층구조 무관 앞
#soup('a')[0].previous # 계층구조 무관 뒤


## 처음 나오는 해당 태그 객체 반환
#soup.find('p')
#s1 =soup.find('a')['href'] # a 태그에서 href 해당하는 값을 가져옴
#print(s1)

## 전체 문서에서 태그를 검색하여 리스트 형태로 반환
#soup.find_all(id='link3')
#soup.find_all('p')
#s2 = soup.find_all(class_='sister')
#print(s2)


## 웹툰에서 가져오기 실습
#from urllib.parse import urljoin
#from urllib.request import urlopen
#import webbrowser

#url= "http://comic.naver.com/webtoon/list.nhn?titleId=449854&weekday=wed"

#data = urlopen(url)
#soup = BeautifulSoup(data, 'html.parser')

#cartoons = soup.find_all('td',{'class':'title'})
#print("-----------------------------------")
#for i in range(len(cartoons)):
#    title = cartoons[i].find('a').string
#    ref = cartoons[i].find('a')['href']
#    tempurl=urljoin(url,ref)
#    print(title,"  ",tempurl)
#    #webbrowser.open_new(tempurl)



#print("-----------------------------------")


#class crawler:
#    def crawl(self, pages, depth=2):
#        for i in range(depth):
#            newpage = set()
#            for page in pages:
#                try:
#                    c = urllib.request.urlopen(page)
#                except:
#                    print("Could not open %s" %page)
#                    continue
#                # encoding 옵션
#                soup = BeautifulSoup(c.read(), from_encoding="utf-8")
#                print('Found %s' %page)
#            links = soup('a')

#            for link in links:
#                if('href' in dict(link.attrs)):  # a 에 들어갈 수 있는 속성 중 href 찾음
#                    url = urllib.parse.urljoin(page, link['href'])
#                    if url.find("'")!=-1 : continue
#                    url = url.split("#")[0]
#                    if url[0:4]=='http': # http로 시작하는 url은 add
#                        newpage.add(url)
#            pages = newpage

#pagelist=['http://naver.com']
#crawler=crawler()
#crawler.crawl(pagelist)




#### XML 파싱 #####

f = open('test.xml')
xml = f.read()
soup = BeautifulSoup(xml)
for node in soup.findAll('node'):
    print("Node: "+node.string)
    print("Attr!: "+node['attr1'])

f=open('song.xml', encoding='utf-8')
xml = f.read()
soup = BeautifulSoup(xml)
for nodes in soup.test('song'):
    for node in nodes:
        print(node.string)


f = open('alcohol.xml', encoding='utf-8')
xml = f.read()
soup = BeautifulSoup(xml,'html.parser')
for nodes in soup.alcohol('cate1'):
    if nodes['tt']=='안주': # 안주만 출력하려면.
        print('Cate1 : '+nodes['tt'])
        for node in nodes('cate2'):
            print('\tCate2 :' +node['tt'])
            for item in node('item'):
                print('\t\t'+item.string)


# lxml 파서
#soup = BeautifulSoup(xml,'lxml') 


############# json 파싱 ################

import json
data = {1:'a', 2:'b'}
data2 = json.dumps(data) # 파이선 데이터를 json 데이터 형식으로 변환
data3 = json.loads(data2) # json 데이터를 python 데이터로 변환
print(type(data2))
print(type(data3))

data = {1:'우리',2:'나라'}
data2 = json.dumps(data, ensure_ascii=False) # 한글모드를 위한..
print(data2)



s = """
{
"name": "cybaek",
"detail" : { "last": "baek" },
"emails": [ "cybaek@xxx.com", "cybaek@yyy.com" ]
}
"""

data = json.loads(s)

print(data['name'])
print(data['detail'])
print(data['detail']['last'])


class JsonObject:
    def __init__(self,d): 
        self.__dict__ = d # 제이슨 데이터를 dict에 넣어줌

data = json.loads(s, object_hook=JsonObject) # 읽어들일때 이클래스로 후킹하겟당.
print(data.name)
print(data.detail)
print(data.detail.last)
for email in data.emails:
    print(email)