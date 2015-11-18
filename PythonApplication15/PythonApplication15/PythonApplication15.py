from flask import Flask, url_for, redirect

app = Flask(__name__)

# 특정 함수가 호출 되었을 때 경로를 알고 싶음
#with app.test_request_context():
    #print(url_for('get_profile',username='greenjoa'))
    #redirect(url_for('get_profile',username='greenjoa'))
    # 바로 경로를 바꿀 때


# 루트로 접속했을 때 이 함수를 호출하라
@app.route('/')
def hello_world():
    return redirect('/login')
    #return 'hello world'

@app.route('/login')  
def login():
    return 'login'


# url로 들어오는 값을 변수처럼 사용 가능 
@app.route('/profile/<username>')
def get_profile(username):
    return 'profile : ' + username

@app.route('/profile2/', methods=['POST','GET'])
def profile(username=None):
    error=None
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        if not username and not email:
            return add_profile(request.form)
    else:
        error = 'Invalide username or email'
 
    return render_template('profile.html', error=error)



@app.route('/message/<int:message_id>')
def get_message(message_id):
    return 'message_id : %d' % message_id


if __name__=='__main__':
    #app.run()

    app.debug = True # 소스변경과디버거제공
    app.run(host='203.252.166.32', port=5000)