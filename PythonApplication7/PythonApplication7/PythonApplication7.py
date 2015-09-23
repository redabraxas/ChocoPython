
#coding:cp949
#모든 클래스는 object로부터 파생된다
class HousePark:
    lastname="박"
    def __init__(self, name):
        self.fullname=self.lastname+name
    def traval(self,where):
        print("%s,%s여행을 가다."%(self.fullname, where))



class HouseKim(HousePark):
    lastname="김"
    def __init__(self,name,age):
        HousePark.__init__(self,name)
        self.age=age
    def traval(self,where,day):
        HousePark.traval(self,where)
        print("%s, %d살에 %s여행 %d일 가네." %(self.fullname, self.age, where, day))


aa = HousePark("단희")
aa.traval("산")

bb = HouseKim("단희1",22)
HouseKim.traval(bb,"애슐리",23)

class A :
    def __init__(self):
        print("A 생성자 호출")

class B :
    def __init__(self):
        print("B 생성자 호출")

class C(A,B) :
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("C 생성자 호출")



#부모 클래스 반환해주는 수퍼

class A :
    def __init__(self):
        print("A 생성자 호출")

class B(A) :
    def __init__(self):
        super().__init__()
        print("B 생성자 호출")

class C(A) :
    def __init__(self):
        super().__init__()
        print("C 생성자 호출")

class D(B,C):
    def __init__(self):
        super().__init__()
        print("D 생성자 호출")

dd = D()

if issubclass(D,B):
    print("서브클래스맞음")


    
##추상클래스
#from abc import ABCMeta, abstractclassmethod

## 테란은 객체가 없음.
#class Terran (metaclass=ABCMeta):
#    def __init__(self,name):
#        self.name = name
#    @abstractclassmethod
#    def attack(self):
#        pass


#class Tank(Terran):
#    def __init__(self, name, damage):
#        super().__init__(self,name)
#        self.damage=damage
#    def attack(self):
#        print("탱크가 쏩니다.")



#class Marine(Terran):
#    def __init__(self, name, hp):
#        super().__init__(self,name)
#        self.hp=hp
#    def attack(self):
#        print("총을 쏩니다.")


#def Attack(terran):
#    terran.attack()

#t1 = Tank("tank",0)
#t2 = Marine("marine",100)


#tlist=[ Tank("tank1",0),  Tank("tank2",1), Marine("marine1",100), Marine("marine2",200)]
#for item in tlist:
#    Attack(item)




class MyList(list):
    name=""
    def __init__(self,name):
        super().__init__([])
        self.name = name
    def __str__(self):
        return self.name+":"+super().__str__()

   

list1 =MyList("greenjoa")
list1.append(10)
list1.append(30)
list1.append(50)
list1.append(70)
print(list1)


class MyClass:
    def __init__(self, name):
        self.name = name
    def __add__(self, another):
        return self.name + "asdf"+another.name   # 내가만든클래스가앞에: __add__# 내가만든클래스가뒤에: __radd__# 둘다 재정의하던지!m1 = MyClass("단희")m2  = MyClass("단희2")print(m1+m2)