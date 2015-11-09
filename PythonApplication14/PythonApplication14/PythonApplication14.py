
 #### 디비 실습 ####

import sqlite3

from werkzeug import check_password_hash, generate_password_hash


def init_db():
   
    db = get_db()
    #### sql 파일 읽어와 실행 ####
    with open('schema.sql') as f:
        db.cursor().executescript(f.read())
        db.commit() # 디비 반영


 # 디비 연결
def get_db():
    db  =sqlite3.connect("test.db")
    return db

def register():
    db = get_db()
    cur = db.cursor()
    print("=======회원가입========")

    while 1:
        id = input("id: ")
       
        #cur.execute("select count(*) from user where userid='"+id+"';")
        cur.execute("select * from user where userid=?", [id])
        #if cur.fetchone()[0] != 0 :
        #    print("이미 존재하는 아이디입니다.")
        #    continue;
        if cur.fetchone() != None :
            print("이미 존재하는 아이디입니다.")
            continue
        else : break

    name = input("name: ")
    pw = input("pw: ")
    hpw = generate_password_hash(pw)
    insertsql ='''insert into user (userid, username, userpw) values(?, ?, ?)'''
    cur.execute(insertsql, [id, name, hpw])
    db.commit()
    

init_db()

def read():
    db = get_db()
    cur = db.cursor()
    cur.execute("select * from user;") # 커서가 첫행 가르킴
    print(cur.fetchall()) # cursor 다음 모두 가져오기?

def login():
    db = get_db()
    cur = db.cursor()

    id = input("id: ")
    pw = input("pw: ")

    cur.execute("select userpw from user where userid=?", [id])
    temp = cur.fetchone()
    if temp == None :
        print("아이디가 존재하지 않아염")
    else : 
        if check_password_hash(temp[0],pw):
            print("로그인 성공")
        else:
            print("비밀번호가 일치하지 않네염")


while 1:
    print("1 회원가입 2 로그인 ")
    key = int(input())
    if key == 1:
        register()
    else:
        login()
    read()
        



# mysql server
import pymysql as mysql
con = mysql.connect(host='127.0.0.1',
 user='greenjoa', passwd=‘1234',db='my_db', charset='utf8')
cursor = con.cursor()