
#-3- 클래스 생성자 #

class A():
    def __init__(self, a):
        self.a = a
    def show(self):
        print('show:', self.a)

class B(A):
    def __init__(self, b, **arg):
        super().__init__(**arg)
        self.b = b
    def show(self):
        print('show:', self.b)
        super().show()

class C(A):
    def __init__(self, c, **arg):
        super().__init__(**arg)
        self.c = c
    def show(self):
        print('show:', self.c)
        super().show()

class D(B,C):
    def __init__(self, d, **arg):
        super().__init__(**arg)
        self.d = d
    def show(self):
        print('show:', self.d)
        super().show()

## 매개변수 이름과 동일. 순서는 상관 없음
data = D(a=1,b=2,c=3,d=4)
data.show()# 기본적 접근 제어 : public
# 제약을 두고 싶다면class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        # __ 언더바 : private varialbes
        self.__update(iterable)
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    # private copy of original update() method
    __update = update

class MappingSubclass(Mapping):
    # 오버라이딩ㄴㄴ 오버로드 -> 부모호출ㄴ
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)list = [1,2,3]ms = MappingSubclass(list)key=[4,5,6]value=['a','b','c']ms.update(key,value)print(ms.items_list)m = Mapping(list)m.update(value)print(m.items_list)import sys## 예외처리
try:
    number1 = float(input("enter a number : "))
except:
    error = sys.exc_info()[0]
    print(error)
    sys.exit()
finally:
    print("Done")


try:
    number1 = float(input("enter a number : "))
except:
    error = sys.exc_info()[0]
    print(error)
    sys.exit()
finally:
    print("Done")


try:
    result = number1 / number2
    print(result)
except ZeroDivisionError as e :
    print(e)
    print("The answer is infinity")
except:
    error = sys.exc_info()[0]
    print(error)
    sys.exit()
finally:
    print("Done")