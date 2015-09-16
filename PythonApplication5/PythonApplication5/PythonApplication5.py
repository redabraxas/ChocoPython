#fileName= "greenjoa.txt"
#myFile=open(fileName, "w")
#myFile.close()

## w+는 읽고쓰기
## a 는 파일내용추가
## b는 바이너리파일로열기

#WRITE="w"
#READ ="r"

#myFile=open(fileName, mode = WRITE)
#myFile.write("HI THERE!\n")
#myFile.write("How are you?\n")

#myFile.close()


#fileName= "test.txt"
#myFile=open(fileName,mode = READ)
### 전체 파일 읽기
#fileContents = myFile.read()
#print(fileContents)
#myFile.close()

## 자동해제됨(파일 클로즈)
#with open(fileName, READ) as myFile:
#    fileContents = myFile.read()
#    print(fileContents)

#myFile=open(fileName,mode = READ)
#while True:
#    ## 라인단위로 읽어오기
#    content = myFile.readline()
#    # 파일의 끝일 경우 None을 리턴
#    if not content : break
#    print(content)
#myFile.close()

#myFile=open(fileName,mode = READ)
#content = myFile.readlines()
#for line in content:
#    print(line)
#myFile.close()
 


############## 실습 ############
#fileName= "greenjoa.txt"
#with open(fileName, "w+") as myFile:
#    myFile.write("201311227 엄단희\n")
#    myFile.write("201311227 김단희\n")
#    myFile.write("201311227 박단희\n")
#    myFile.write("201311227 이단희\n")

#with open(fileName, "r") as myFile:
#    #content = myFile.readlines()
#    for line in myFile:
#        print(line)


### 정제된 데이터 
fileName1= "파일입출력예제1.txt"
fileName2= "Monica.txt"


#모니카 대사만 빼오기?
with open(fileName1, "r") as myFile, open(fileName2, 'w') as Monica:
    for content in myFile:
        (role, etc) = content.strip().split(":")
        if role == 'Monica':
            Monica.write(etc+"\n")


#모니카파일 읽어오기
with open(fileName2, "r") as Monica:
    for line in Monica:
        print(line)


#### 정제되지않은 데이터
fileName1= "파일입출력예제2.txt"
fileName2= "Monica2.txt"


#모니카 대사만 빼오기?
with open(fileName1, "r") as myFile, open(fileName2, 'w') as Monica:
    for content in myFile:
        (role, etc) = content.strip().split(":", 1)
        if content[:6] == 'Monica':
            Monica.write(content+"\n")


#모니카파일 읽어오기
with open(fileName2, "r") as Monica:
    for line in Monica:
        print(line)



## 주인공 롤 리스트에 저장
fileName1= "파일입출력예제1.txt"

RoleList=[]
#모니카 대사만 빼오기?
with open(fileName1, "r") as myFile:
    for content in myFile:
        (role, etc) = content.strip().split(":", 1)
        RoleList.append(role)

print(RoleList)


#모니카파일 읽어오기
with open(fileName2, "r") as Monica:
    for line in Monica:
        print(line)






####### 피클사용
import pickle
fileName1= "파일입출력예제1.txt"
fileName3= "Monica3.txt"

RoleList2=[]
#모니카 대사만 빼오기?
with open(fileName1, "r") as myFile, open(fileName3, 'wb') as Monica:
    for content in myFile:
       (role, etc) = content.strip().split(":", 1)
       RoleList2.append(role)
    pickle.dump(RoleList,Monica)

with open(fileName2, "rb") as Monica:
    result = pickle.load(Monica)
    print(result)








#import csv
#fileNmae="test.txt"
#READ="r"
#with open(fileName,READ) as myFile:
#    dataFromeFile = csv.reader(myFile)
#    for currentRow in dataFromFile :
#        print(currentRow)


### csv 파일다루기
#import csv
#fileName = "test.txt"
#READ = "r"
#with open(fileName, READ) as myFile :
#    dataFromFile = csv.reader(myFile)
#    for currentRow in dataFromFile :
#        for currentWord in currentRow :
#            print(currentWord)# ## 목록연결해주는 join# with open(filename, READ) as myFile :  
#    dataFromFile = csv.reader(myFile)
#    for currentRow in dataFromFile :
#        print(",".join(currentRow))