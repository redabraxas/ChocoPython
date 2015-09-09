
# List=[] Tuple=() Dic={}

dic1={}
dic2=dict()
dic={'name':'pey','phone':'01099993323','birth':'1118'}

print(dic['name'])

print(dic)


a={'name':'pey','phone':'01099993323','birth':'1118'}
b=a.keys()
print(b)

b=list(a.keys())
print(b)

c=a.values()
print(c)

c=list(a.values())
print(c)

d=a.items()
print(d)

# a.clear()

name=a.get('name','none')
print(name)

if 'name' in a:
    print(name)



movie={"홍길동":{"베테랑":"5.0","암살":"4.5"},"고길동":{"베테랑":"3.5","암살":"4.1"}}


# 홍길동이 암살에몇점?
score= movie.get('홍길동').get('암살')
print(score)

print(movie['홍길동']['암살'])


#set : 교집합,합집합,차집합을 지원해준다.

s1=set([1,2,4,4,6,4,3,5,2])
print(list(s1))

#answer = input("Would you like express shipping?")
#if answer.lower() == "yes" :
#    print("That will be an extra $10")

#deposit=input("How much would you like to deposit?")
#if float(deposit)>100:
#    print("you get a free toaster!")
#else:
#    print("Enjoy your mug!")
#print("Have a nice day")

pocket=['paper','cellphone','money']

if 'money' in pocket:
#    print("택시타고가")
    pass
else:
    print("걸어가")

#처리 내용이 한줄인 경우,
if 'money' in pocket: pass


### for 

for steps in [1,2,3,4,5] :
    pass

#a=[(1,2),(3,4),(5,6)]
#for (first,last) in a:
#    print(first+last)


#marks = [90,5,67,45,80]
#for number in range(len(marks)):
#    print(number)


for i in range(2,10):
    for j in range(1, 10):
        print("%d*%d=%d" %(i,j,i*j), end=" ")
    print("")



a=[1,2,3,4]
result =[]
result=[num*3 for num in a]
result=[num*3 for num in a if num % 2 == 0]
result=[x*y for x in range(2,10) for y in range(1,10)]


import turtle
#for steps in range(100) :
#    turtle.forward(100)
#    turtle.right(90)
#    turtle.left(40)
#    turtle.backward(30)

#for steps in range(4):
#    turtle.forward(100)
#    turtle.right(90)
#    for moresteps in range(4):
#          turtle.forward(50)
#          turtle.right(90)

nSides =13

#for steps in range(100):
#    turtle.forward(100)
#    turtle.right(360/nSides)
#    for moresteps in range(nSides):
#          turtle.forward(50)
#          turtle.right(360/nSides)

for steps in ['red','blue','green','black']:
    turtle.color(steps)
    turtle.forward(100)
    turtle.right(90)


prompt ="1.Add \n2.Del \n3.List \n4.Quit \n\nEnter number:"

number=0
while number !=4:
    print(prompt, end="")
    number=int(input())