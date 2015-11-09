########## DB #############


## 서버급은 아니고 그냥 간단하게 로컬에서 사용
## 웹서버는 오라클 같은 걸 사용 
import sqlite3

# 데이터베이스 파일 반영하는 객체
# 경로에 파일 생성. 이미 존재하면 그대로 사용
con =sqlite3.connect("test.db")

## moemory: 메모리 상에 디비를 만들 수 있음
# 연결 종료 시 작업내용 없어짐
# 연산속도 빠름
#con = sqlite3.connect(":memory:")

cur = con.cursor()


## 테이블 삭제 (존재하면)
#dropsql='''drop table if exists phonebook;'''
#cur.execute(dropsql)


## 테이블 생성( 존재하지 않으면)
#sql='''create table if not exists
#        phonebook(name text, phoneNum text);'''
#cur.execute(sql)



######## 레코드 삽입 #######

## 방법1 : 일반적 삽입
#insertsql ='''insert into phonebook
#    values('greenjoa1','010-1111-2222');'''
#cur.execute(insertsql)


## 방법2 : -? 를 통한 삽입
## 인자 전달 순서에 맞추어 시퀀스 객체 전달
#name ='greenjoa2'
#phoneNumber='010-2222-2222'
#insertsql ='''insert into phonebook values(?,?);'''
#cur.execute(insertsql, (name,phoneNumber))


## 방법3 : 인자를 통한 삽입
## 인자에 이름을 부여해서 수행하는 방법
#name='greenjoa3'
#phoneNumber='010-3333-3333'
#insertsql='''insert into phonebook values(:inputName, :inputNum);'''
#cur.execute(insertsql,
#    {"inputNum":phoneNumber, "inputName":name})


## 방법4 : iterator 객체를 통한 삽입
#insertsql = '''insert into phonebook values(?,?);'''
#datalist=(('greenjoa4','010-4444-4444'),
#          ('greenjoa5','010-5555-5555'))
#cur.executemany(insertsql, datalist)


# 방법5 : 제너레이터를 통한 삽입
#def dataGenerator():
#    datalist=(('Greenjoa6','010-6666-6666'),
#              ('Greenjoa7','010-7777-7777'))
#    for item in datalist:
#        yield item # yield: return과 같이 값 반환. 종료 ㄴㄴ

#cur.executemany(insertsql, dataGenerator())



######## 레코드 조회 #######

cur.execute("select * from phoneBook;") # 커서가 첫행 가르킴
#cur.fetchone() # cursor 다음 꺼 하나를 가져온다
#cur.fetchmany(2) # cursor 다음 2개 가져오기?
#cur.fetchall() # cursor 다음 모두 가져오기?
for row in cur:
    print(row)
    print(row[0])


###### 트랜잭션 ######
# 데이터베이스에서 논리적 작업의 단위
# 개별 작업이 하나 연산처럼 묶어서 처리.
# 트랜잭션 시작 -> 커밋(디비에영구저장)/롤백(수행이전상태)
#con.commit() # 데이터베이스 반영
#con.isolation_level =None # 자동으로 커밋 설정


####### 레코드 정렬 #######
# order by
cur.execute("select * from phoneBook order by name;") #오름차
cur.execute("select * from phoneBook order by name desc;") #내림차
print(cur.fetchall())


## 사용자 지정 정렬
# 대문자든 소문자든 같게 취급하고싶다.
def OrderFunc(str1,str2):
    s1 =str1.upper() # 둘다 대문자로 바꾸고
    s2 =str2.upper()
    return (s1>s2)-(s1<s2) # 앞이크면- 같으면0 뒤가크면+

con.create_collation('myordering',OrderFunc)
cur.execute("select * from phoneBook order by name collate myordering;")
print(cur.fetchall())


####### 내장 집계 함수 #######

con.execute("insert into phonebook(phoneNum) values('010-9999-9999');")
cur.execute("select count(*) from phoneBook;")
print(cur.fetchone()[0])

# name에 해당하는 속성이 null이 아닌 것만 반환
cur.execute("select count(name) from phoneBook;")
print(cur.fetchone()[0])

cur.execute('''create table if not exists
        user (name text, age int);''')


cur.execute('''insert into user
    values('단희1','22');''')
cur.execute('''insert into user
    values('단희2','15');''')
cur.execute('''insert into user
    values('단희3','41');''')
cur.execute('''insert into user
    values('단희4','29');''')
cur.execute('''insert into user
    values('단희5','46');''')
cur.execute('''insert into user
    values('단희6','75');''')
cur.execute('''insert into user
    values('단희7','33');''')


cur.execute('''select max(age) from user;''')
print(cur.fetchone()[0])


## 사용자 집계 함수

class Average:
    def __init__(self):
        self.sum =0
        self.cnt=0
        
    # 반드시 들어가야하는 step, finallize
    # step : 각각의 value 값이 들어오는 것. 이 단계마다무엇을?
    # value 인자는 몇 개든 가능.. !
    def step(self, value):
        self.sum +=value
        self.cnt +=1
        
    # finalize : 최종적으로 반환하는 값
    def finalize(self):
        return self.sum/self.cnt

con.create_aggregate("avg",1,Average) # DB에 등록
cur.execute("select avg(Age) from user;")
print(cur.fetchone()[0])


####### 사용자정의 자료형 #######

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Point 객체의 내용 출력
    def __repr__(self):
        return "Point(%f, %f)" % (self.x, self.y)

# 클래스 객체에서 SQLite3 입력 가능한 자료형으로 변환
def PointAdapter(point):
    return "%f:%f"%(point.x, point.y)
# SQLite3에서 조회한 결과를 클래스 객체로 변환
def PointConverter(s):
    x, y = list(map(float, s.decode().split(":")))
    return Point(x,y)

# 클래스 이름과 변환 함수 등록
sqlite3.register_adapter(Point, PointAdapter)
# SQL 구문에서 사용할 자료형 이름과 변환 함수 등록
sqlite3.register_converter("point", PointConverter)


p1 = Point(4,3)
p2 = Point(3,4)

con1 = sqlite3.connect(":memory:")
cur1 = con1.cursor();

cur1.execute("create table test(p point);")
cur1.execute("insert into test values(?);", (p1,))
cur1.execute("insert into test(p) values(?);", (p2,))
cur1.execute("select p from test")
print(cur1.fetchone())