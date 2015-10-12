


import os, sys

## 다른 파이썬 파일 실행
#os.system('python test.py 1 2 3')
## 경로 출력
#print(sys.path)


#class Student:
#    def __init__(self, name, age):
#        self.name = name
#        self.age =age
#    def show(self):
#        print(self.name, ":", self.age)


#st1 = Student("엄단희",22)
#st1.show()

#import pickle
#f = open("test.txt", "wb")
#pickle.dump(st1,f)
#f.close()

#f = open("test.txt", 'rb')
#data = pickle.load(f)
#print(data)

#Student.show(data)
#data.show()

##print(os.environ)
#print(os.getcwd())
#os.chdir("..")
#print(os.getcwd())

#print(list(os.walk("..")))


#현재 디렉토리에 만든 후 txt파일 복사
import shutil
# 폴더가 잇는가?

if os.path.exists('sample') == False:
    os.mkdir("sample")


samplePath = os.path.abspath("sample")

#for (path, dir, files) in os.walk('.'):
#    for dirname in dir:
#        if dirname.find("sample") == -1:
#            os.mkdir("sample")
            

for (path, dir, files) in os.walk('.'):
    if path != "sample":
        for filename in files:
            if(filename.find('.txt') != -1):                shutil.copy(path+"/"+filename, samplePath+"/"+filename)os.path.expanduser('~\\python.exe')os.path.expandvars('$JAVA_HOME\\python.exe')