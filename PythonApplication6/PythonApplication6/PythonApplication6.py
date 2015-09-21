
#coding:cp949
#class Service:
#    secret="영구는 배꼽이 두개다" #클래스변수
#    def _init_(self, name, value = 0):
#        #초기화하면서 멤버를만들어줄수도 있음
#        self.name=name # 인스턴스변수
#        self.value=value
#        self.secret=secret
#    #self= c,java에서 this랑 같은 개념
#    def sum(self,a,b):
#        result=a+b
#        print("%s+%s=%s 입니다."%(a,b,result))

#pey= Service()
#print(pey.secret)

#pey.sum(1,1)
#Service.sum(pey,1,1)

#Service.age=0
#print(Service.age)


class Movie:
    '''영화클래스입니다.'''
    count=0
    title="암살"
    director="최동훈"
    def __init__(self,title,director):
        print(self.title+"영화가 생성되었슴다.")
        self.title = title
        self.director = director
        Movie.count +=1
    def __del__(self):
        print(self.title+"영화가 삭제되었습니다.")
    def showInfo(self):
        print("영화제목:  "+self.title+"\n영화감독: "+self.director)
    @staticmethod
    def showCount():
        print(Movie.count)

    @classmethod
    def showCount2(cls):
        print(cls.count)


#Movie.__init__(movie1,"베테랑","류승환")
#Movie.showInfo(movie1)
#movie1.actor="황정민"
#print(movie1.actor)

#movie2 =Movie()
#movie2.__init__("간신","누구징")
#movie2.showInfo()
# print(movie2.actor) #속성이없어서 에러남



movie3=Movie("베테랑3","류승완3")
print(movie3.title)
print(movie3.__doc__)

movie4=Movie("베테랑4","류승완4")
#대입연산을하면 얕은복사-> 같은 주소를 가르키고있는형태
print(type(movie4))
movie4= movie3
movie4.showInfo()

print(id(movie3))
print(id(movie4))


movie5=Movie("베테랑5","류승완5")
movie6=Movie("베테랑6","류승완6")


movie5.showCount2()
movie6.showCount()
