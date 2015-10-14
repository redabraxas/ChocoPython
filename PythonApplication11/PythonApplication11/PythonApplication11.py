
## 정규표현식을지원하는모듈
import re

# 정규식 객체 생성
p = re.compile('ab*')
p = re.compile('ab*', re.IGNORECASE)
# r: 문자그대로인식
# 그냥 \ 그대로 인식
p = re.compile(r'\section')
p = re.compile(r'\\section')Result = p.match('abbbb')p = re.match('ab*','abbbb')# 스트링 전체에서 일치하는 부분 검색해서반환pattern = re.compile("d")
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
result = pattern.match("dog",1)print(result.group())##공백도 슬러시사용해야하는데ㅔ# r 사용시 그대로str ='''sample1.Sample2.Sample3.'''# 멀티랑니 적용p1 =re.compile("^.*", re.S)result = p1.search(str)print(result.group())# () 이거당 그룹 하나# \s 공백도 포함str=" abc 1234 xyz "
pattern = re.compile("\s*[a-zA-Z]+\s+(\d+)+\s+([a-zA-Z]+)\s*");
result = pattern.match(str)
print(result.group(1))
print(result.group(2))# fullmath 전체스트링 정규식 일치pattern = re.compile("o[gh]")
result = pattern.fullmatch("dog")
result = pattern.fullmatch("ogre")
result = pattern.fullmatch("doggie",1,3)print(result)# 정규식 만족하는부분에서 분할된리스트반환# 문자가 아닌것들로 스플릿?pattern = re.compile("\W+")
result = pattern.split('words, words, words.')
result = pattern.split('words, words, words.',2)print(result)pattern = re.compile("x*")
result = pattern.split('axbc')print(result)# sub(변호나문자,문자열)result = re.sub(r'\W','','a:b:c, d.')print(result)str = '<a href="index.html">HERE</a><font size="10">'
result = re.search(r'href="(.*)">', str)
print(result.group(1))
# 물음표를 찍으면 최소매칭.
result = re.search(r'href="(.*?)">', str)
print(result.group(1))


num = "940923-2049518"

result = re.fullmatch('(\d{6})-(\d{7})',num)
print(result.group(1))
print(result.group(2))

