



##list =[1,2,3]
##print(dir(list))
#data = list(enumerate("123"))
#print(data)

##def positive(l):
##    result = []
##    for i in l:
##        if i > 0:
##            result.append(i)
##            return result

##print(positive([1,-3,2,0,-5,6]))

#def even(l):
#        return l%2 ==0

#print(list(filter(even,[1,-3,2,0,-5,6])))

#a=3
#print(id(3))
#print(id(a))
## 다 참조하고 있는 형태..

#print(int('111111111',2))


#sum = lambda a,b : a+b

#print(list(filter(lambda l : l%2==0,[1,-3,2,0,-5,6])))

#a = [1,2,3] 
#b = list(a) # 아예새로만들어짐
#c = a # 동일한 개념(포인터)

#c.append(4)

#print(id(a))
#print(id(b))
#print(id(c))
#print(a)
#print(b)
#print(c)


#print(list(map(lambda a: a*2, [1,2,3,4])))

#eval # 문자열 연산 결과 반환

#print(eval(repr("hi".upper())))


#ml = [1,-3,2,0,-5,6, 1, 3, 10, -4]
#print(sorted(ml)) # 바뀌진 않음
#print(ml)
#print(ml.sort()) # 바뀜
#print(ml)

#aa  = list(zip([1,2,3],[4,5,6],[7,8,9]))
#print(aa)
#bb = list(zip("abc","def"))
#print(bb)


data = { "홍길동":[80,70,60,90],
        "김길동":[24,35,18,10],
        "고길동":[10,20,8,5]}


#for i in data:
#    data[i].sort()

#print(data)



print((filter(lambda i : data[i].sort(), data)))