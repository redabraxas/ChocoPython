
## 정규표현식을지원하는모듈
import re

# 정규식 객체 생성
p = re.compile('ab*')
p = re.compile('ab*', re.IGNORECASE)
# r: 문자그대로인식
# 그냥 \ 그대로 인식
p = re.compile(r'\section')
p = re.compile(r'\\section')


Result = p.match('abbbb')
p = re.match('ab*','abbbb')


# 스트링 전체에서 일치하는 부분 검색해서반환
pattern = re.compile("d")
result = pattern.search("dog")
print(result.group())
result = pattern.search("dog",1)
print(result)

result = re.search("\\\\", "C:\\test")
print(result.group())
result= re.search(r"\\", "C:\\test")
print(result.group())

pattern = re.compile("og")
result = pattern.match("dog")
result = pattern.match("dog",1)
print(result.group())

##공백도 슬러시사용해야하는데ㅔ
# r 사용시 그대로


str ='''sample1.
Sample2.
Sample3.'''
# 멀티랑니 적용
p1 =re.compile("^.*", re.S)
result = p1.search(str)
print(result.group())


# () 이거당 그룹 하나
# \s 공백도 포함
str=" abc 1234 xyz "
pattern = re.compile("\s*[a-zA-Z]+\s+(\d+)+\s+([a-zA-Z]+)\s*");
result = pattern.match(str)
print(result.group(1))
print(result.group(2))

# fullmath 전체스트링 정규식 일치
pattern = re.compile("o[gh]")
result = pattern.fullmatch("dog")
result = pattern.fullmatch("ogre")
result = pattern.fullmatch("doggie",1,3)
print(result)

# 정규식 만족하는부분에서 분할된리스트반환
# 문자가 아닌것들로 스플릿?
pattern = re.compile("\W+")
result = pattern.split('words, words, words.')
result = pattern.split('words, words, words.',2)
print(result)

pattern = re.compile("x*")
result = pattern.split('axbc')
print(result)

# sub(변호나문자,문자열)
result = re.sub(r'\W','','a:b:c, d.')
print(result)





str = '<a href="index.html">HERE</a><font size="10">'
result = re.search(r'href="(.*)">', str)
print(result.group(1))
# 물음표를 찍으면 최소매칭.
result = re.search(r'href="(.*?)">', str)
print(result.group(1))


num = "940923-2049518"

result = re.fullmatch('(\d{6})-(\d{7})',num)
print(result.group(1))
print(result.group(2))


## findall : 만족하는 모든 것을 반환
str = '''Window
Unix
Linux
Solaris'''
# ^ 시작 . 줄바꿈을 제외한 문자 + 1개 이상
p1 = re.compile('^.+', re.M)
# re.M = 멀티라인 
print(p1.findall(str))
p2= re.compile('^.+', re.S)
print(p2.search(str))

## Group 이름 지정
m = re.match(r"(?P<first>\w+) (?P<last>\w+)", "Malcolm Reynolds")
print(m.group('first','last'))
print(m.groups())
print(m.groupdict()) # ditionary 출력

## Group 디폴트값
m = re.match(r"(\d+)\.?(\d+)?","24")
print(m.groups())
print(m.groups(0))


p = re.compile(".+:") # : 앞에 하나 이상 아무것다 올 수 잇다
m = p.search("http://google.com")
print(m.group()) # http: 이 나옴.

# : 앞에 해당하는 것만 결과 값으로 주겠다.
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())

## 해당 정규식과 매치되어도 해당 문자열은 통과되지 않음
p= re.compile('.*[.](?!bat$|exe$).*$')

import os, glob
os.chdir('C:\\')
a = glob.glob('.*[.](?!bat$|exe$).*$') # 현재 디렉토리 반환
print(a)

# abcdef 를 찾되 , def만 반환
p = re.compile("(?<=abc)def")
m = p.search("abcdefasdf")
print(m.group())

# - 뒤의 글자만 반환
m = re.search('(?<=-)\w+', "spam-egg")
print(m.group())


# 매치되는 스트링의 사작과 긑 인덱스 반환 
email = "tony@tiremove_thisger.net"
m = re.search("remove_this", email)
print(repr(m.start()) + "  " + repr(m.end()))
result = email[:m.start()] + email[m.end():]
print(result)

# 그냥 매치 정보 출력 함수
def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

# 다섯개의 문자열이 저렇게 끝나야한다.
valid = re.compile(r"^[a2-9tjqk]{5}$")
d1 = displaymatch(valid.match("akt5q"))
print(d1)

text = """Ross: McFluff: 834.345.1254: 155 Elm Street
Ronald: Heathmore: 892.345.3428 436: Finley Avenue
Frank: Burger: 925.541.7625 662: South Dogwood Way
Heather: Albrecht: 548.326.4584 919: Park Place"""

# 엔터키를 기준으로 엔트리를 만들엇당.
entries = re.split("\n", text)
result = [re.split(":?", entry, 4) for entry in entries]
print(result)



## url 오픈
import urllib.request

with urllib.request.urlopen('http://www.python.org/') as f:
    #print(f.read())
    #print(f.read(300))
    #print(f.read(300).decode("utf-8"))
    # 타이틀 받아오기
    content = f.read().decode("utf-8")
    result = re.search(r'<title>(.*)</title>', content)
    print(result.group(1))




   

## url 파싱
#from urllib.parse import urlparse
#result = urlparse('http://search.naver.com/search.naver?where=nexearch&query=urllib.parse&sm=top_hty&fbm=1&ie=utf8')
#print(result)
#print(result.scheme)
#print(result.geturl())
