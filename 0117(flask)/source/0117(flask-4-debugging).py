'''
서버가 아닌 콘솔에서 확인

test_request_context() 
- Flask 객체에 있는 메서드
- HTTP 요청이 가능한 매서드(일종의 디버깅)


url_for('View 함수명', args...)
'''

from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>hello debugging world</h1>'

# 콘솔에 주소를 반환
'''
if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('hello'))
'''


@app.route('/user/<username>')
def get_user(username):
    return '<h1>username is %s</h1>' %username

# 콘솔에 주소를 반환
if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('get_user', username = 'kim'))