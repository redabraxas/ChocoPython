
#coding:cp949
#��� Ŭ������ object�κ��� �Ļ��ȴ�
class HousePark:
    lastname="��"
    def __init__(self, name):
        self.fullname=self.lastname+name
    def traval(self,where):
        print("%s,%s������ ����."%(self.fullname, where))



class HouseKim(HousePark):
    lastname="��"
    def __init__(self,name,age):
        HousePark.__init__(self,name)
        self.age=age
    def traval(self,where,day):
        HousePark.traval(self,where)
        print("%s, %d�쿡 %s���� %d�� ����." %(self.fullname, self.age, where, day))


aa = HousePark("����")
aa.traval("��")

bb = HouseKim("����1",22)
HouseKim.traval(bb,"�ֽ���",23)

class A :
    def __init__(self):
        print("A ������ ȣ��")

class B :
    def __init__(self):
        print("B ������ ȣ��")

class C(A,B) :
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("C ������ ȣ��")



#�θ� Ŭ���� ��ȯ���ִ� ����

class A :
    def __init__(self):
        print("A ������ ȣ��")

class B(A) :
    def __init__(self):
        super().__init__()
        print("B ������ ȣ��")

class C(A) :
    def __init__(self):
        super().__init__()
        print("C ������ ȣ��")

class D(B,C):
    def __init__(self):
        super().__init__()
        print("D ������ ȣ��")

dd = D()

if issubclass(D,B):
    print("����Ŭ��������")


    
##�߻�Ŭ����
#from abc import ABCMeta, abstractclassmethod

## �׶��� ��ü�� ����.
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
#        print("��ũ�� ���ϴ�.")



#class Marine(Terran):
#    def __init__(self, name, hp):
#        super().__init__(self,name)
#        self.hp=hp
#    def attack(self):
#        print("���� ���ϴ�.")


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
        return self.name + "asdf"+another.name   # ��������Ŭ�������տ�: __add__# ��������Ŭ�������ڿ�: __radd__# �Ѵ� �������ϴ���!m1 = MyClass("����")m2  = MyClass("����2")print(m1+m2)