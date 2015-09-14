## 오늘은 즐거운 함수시간


def sum_and_mul(a,b):
    return a+b, a*b

answer = sum_and_mul(10,30)
answer1, answer2 = sum_and_mul(3,29)
print(answer)
print(answer1)

# 디폴트설정은 뒤부터~
def say_myself(name,old,man=True):
    print("나의 이름은 %s 입니다." %name)
    print("나이는 %d살입니다"%old)
    if man:
        print("남자입니다")
    else:
        print("여자입니다")
    
say_myself("바보",23)


#import printData

##coding:cp949
#data =['고길동',['베테랑',['류승완','황정민','유아인'],'암살',['전지현','하정우']], 
#      '홍길동',['뷰티인사이드',['이진욱','박서준'],'베테랑',['류승완','황정민','유아인'],'앤트맨'],
#      '김길동',['인사이드아웃','암살',['전지현','하정우'],'오피스']]


#printData.printData(data)

import os

#help(os.mkdir)

#print(os.getcwd())
##os.mkdir("sample")
os.chdir("./sample")
#print(os.getcwd())

# 패키지를 만드는 과정
#os.system("python setup.py sdist")

# 패키지를 설치하는 과정
os.system("python setup.py install")