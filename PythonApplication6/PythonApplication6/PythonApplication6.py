
#coding:cp949
#class Service:
#    secret="������ ����� �ΰ���" #Ŭ��������
#    def _init_(self, name, value = 0):
#        #�ʱ�ȭ�ϸ鼭 �����������ټ��� ����
#        self.name=name # �ν��Ͻ�����
#        self.value=value
#        self.secret=secret
#    #self= c,java���� this�� ���� ����
#    def sum(self,a,b):
#        result=a+b
#        print("%s+%s=%s �Դϴ�."%(a,b,result))

#pey= Service()
#print(pey.secret)

#pey.sum(1,1)
#Service.sum(pey,1,1)

#Service.age=0
#print(Service.age)


class Movie:
    '''��ȭŬ�����Դϴ�.'''
    count=0
    title="�ϻ�"
    director="�ֵ���"
    def __init__(self,title,director):
        print(self.title+"��ȭ�� �����Ǿ�����.")
        self.title = title
        self.director = director
        Movie.count +=1
    def __del__(self):
        print(self.title+"��ȭ�� �����Ǿ����ϴ�.")
    def showInfo(self):
        print("��ȭ����:  "+self.title+"\n��ȭ����: "+self.director)
    @staticmethod
    def showCount():
        print(Movie.count)

    @classmethod
    def showCount2(cls):
        print(cls.count)


#Movie.__init__(movie1,"���׶�","����ȯ")
#Movie.showInfo(movie1)
#movie1.actor="Ȳ����"
#print(movie1.actor)

#movie2 =Movie()
#movie2.__init__("����","����¡")
#movie2.showInfo()
# print(movie2.actor) #�Ӽ��̾�� ������



movie3=Movie("���׶�3","���¿�3")
print(movie3.title)
print(movie3.__doc__)

movie4=Movie("���׶�4","���¿�4")
#���Կ������ϸ� ��������-> ���� �ּҸ� ����Ű���ִ�����
print(type(movie4))
movie4= movie3
movie4.showInfo()

print(id(movie3))
print(id(movie4))


movie5=Movie("���׶�5","���¿�5")
movie6=Movie("���׶�6","���¿�6")


movie5.showCount2()
movie6.showCount()
