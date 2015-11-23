import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
 abort, render_template, flash
from contextlib import closing

# configuration
DATABASE = 'flask.db'
DEBUG = True
SECRET_KEY = 'development key' #sesson 객체 사용 시
USERNAME = 'admin'
PASSWORD = 'default'
#세션사용, 세션의 안전성 보장


app = Flask(__name__)
app.config.from_object(__name__) # 대문자로 설정된 값을 config 저장

# DB 설정
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    ### 1번째 방법 : 
    #db = connect_db()
    #with open('schema.sql') as f: # 디비 열어서
    #    db.cursor().executescript(f.read()) # 스크립트 실행
    #    # 파일로 실행시킬땐 executescript
    #db.commit() # 디비 반영     ## 2번째 방법 : closing써서 파일,디비 자동으로 종료     with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()init_db()@app.before_request # request 실행전에 호출
def before_request():
    # 디비를 연결한다
    g.db = connect_db() # g: flask 전역 클래스 인스턴스
    # 디비는 다른 function에서도 공유가 되야 하니깐..

@app.teardown_request # request 의 마지막에 호출
def teardown_request(exception):
    # 디비 연결을 닫는다.
    g.db.close()@app.route('/')
def show_entries(): # cursor 객체를 생성한후 질의를 수행하는 비표준 방법
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
        return render_template('login.html', error=error)
@app.route('/add', methods=['POST'])
def add_entry():
     if not session.get('logged_in'):
        abort(401)
     g.db.execute('insert into entries (title, text) values (?, ?)',
        [request.form['title'], request.form['text']])
     g.db.commit()
     flash('New entry was successfully posted')
     return redirect(url_for('show_entries'))
@app.route('/logout')
def logout():
     session.pop('logged_in', None)
     flash('You were logged out')
     return redirect(url_for('show_entries'))

if __name__ == '__main__':
    app.debug=True
    app.run(port=5000)

