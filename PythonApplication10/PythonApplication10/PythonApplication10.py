


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


##현재 디렉토리에 만든 후 txt파일 복사
#import shutil
## 폴더가 잇는가?

#if os.path.exists('sample') == False:
#    os.mkdir("sample")


#samplePath = os.path.abspath("sample")

##for (path, dir, files) in os.walk('.'):
##    for dirname in dir:
##        if dirname.find("sample") == -1:
##            os.mkdir("sample")
            

#for (path, dir, files) in os.walk('.'):
#    if path != "sample":
#        for filename in files:
#            if(filename.find('.txt') != -1):
#                shutil.copy(path+"/"+filename, samplePath+"/"+filename)

#os.path.expanduser('~\\python.exe')
#os.path.expandvars('$JAVA_HOME\\python.exe')


import glob
print(glob.glob("*.txt"))


import glob, os.path

ndir = nfile = 0

def traverse(dir, depth):
    global ndir, nfile
    for obj in glob.glob(dir + '/*'):
        if depth == 0:
            prefix = '|--'
        else:
            prefix = '|' + ' ' * depth + '|--'
        if os.path.isdir(obj):
            ndir += 1
            print(prefix + os.path.basename(obj))
            traverse(obj, depth+1)
        elif os.path.isfile(obj) :
            nfile +=1
            print(prefix + os.path.basename(obj))
        else:
            print(prefix + 'unknown object:',obj)


# 메인 패키지에서 동작될때
if __name__ == '__main__':
    traverse('..', 0)
    print('\n',ndir,'directories,',nfile, 'files')




# 기본모드 w+b -> 바이너리 바꿔줘야함
#import tempfile
#with tempfile.TemporaryFile('w+', delete=False) as fp:
#    fp.write("heelo world")
#    fp.seek(0)
#    data = fp.read()
#    print(data)
#    print(fp.name)


import time;

t1 = time.time()

a =time.strftime("%B %dth %A %I:%M", time.localtime())
print(a)


time1 = time.ctime(1234567)
print(time1)
print(time.strftime(time1))


import calendar
calendar.calendar(2000)
calendar.prcal(2000)


print(calendar.monthrange(2015,10))
print(calendar.monthrange(1994,9))


import random

#중복없이 무작위로 뽑아줌

#rr = random.sample(range(100),10)
#print(rr)
#rrr = random.shuffle(rr)
#rrrr= random.choice(rrr)
#print(rrrr)



weighted_choices = [('Red', 3), ('Blue', 1), ('Yellow', 2), ('Green', 4)]
population = [val for val, cnt in weighted_choices for i in range(cnt)]
datalist =[]
for val, cnt in weighted_choices:
    for i in range(cnt):
        datalist.append(val)

print(population)

import webbrowser
url = 'http://google.com'
webbrowser.open_new_tab(url)
webbrowser.open_new(url)