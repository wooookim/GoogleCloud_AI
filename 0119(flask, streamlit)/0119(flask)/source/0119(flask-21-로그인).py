from flask import Flask, request, session, redirect, make_response, url_for

app = Flask(__name__)

app.secret_key = 'jeju1234!'

# 최초 view 함수, session을 통한 로그인 결과도 갖고 있음
def index():
    if 'userid' in session:
        userid = session['userid']
        return '<h1> logged in as '+ userid +'</h1>'
    else:
        response = make_response('<h1> hello flask world </h1>')
    return response

app.add_url_rule('/', 'index', index)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        # 유효성 검사
        # DB에 id가 존재하면 session에 담고, 없으면 회원가입 페이지로 이동
        
        session['userid'] = request.form['userid']
        return redirect(url_for('index'))
    return'''
        <h2>로그인</h2>
        <form method = 'POST'>
            <p><input type = text name = userid /></p>
            <p><input type = submit value = login /></p>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('userid', None)
    return redirect(url_for('index'))




if __name__ == '__main__':
    app.run()