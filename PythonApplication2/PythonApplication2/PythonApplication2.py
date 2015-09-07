data=['a','b','c',['abcd','efg']]
print(data[0]);
print(data[-1]);
print(data[-1][1]);

b=[1,2,3]
c=['life','is','too','short']

## 연결
f=b+c
print(f)
## 세번 반복
print(b*3)

guests=['a','b','c','d']
print(guests)
guests[0]='greenjoa'
print(guests)
guests[1]=['greenjoa1','green2']
print(guests)
guests[1:2]=['greenjoa','green2']
print(guests)

guests.insert(2,'e')
guests.append('greenjoa2')
print(guests)


## 데이터 없으면 에러발생
print(guests.index('c'))



data=['choco1','choco2','choco3']
data.insert(1,'1234')
data.insert(3,'5678')
data.insert(5, 'abcd')
print(data)


# in 다음에는 리스트가 들어감.
#for setps in range(4) :
#  print(guests[setps])

for steps in data :   
    if isinstance(steps,list) :
        for step in steps :
            print(step)
    else :
         print(steps)



for steps in data :
    print(steps)

data.sort()
print(data)
data.reverse()
print(data)


#즐거운 파이썬시간~~~ 쏠팅을해요
data3=[43,42,65,80,19,28,64,92,41,59,61,34,97,78]

data3.sort()
data3.reverse()

print(data3[0:5])

##팝팝 버블팝!!!

data3.extend([50,60])
print(data3)

data3.append([50,60])
print(data3)