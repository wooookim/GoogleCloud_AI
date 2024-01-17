'''
routing

'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_flask():
    return '<h1> hello flask world </h1>'

@app.route('/main')
def hello_main():
    return '<h1> this is main page </h1>'

'''
routing - Variable rules

<>
- 데이터를 나타냄
- 데이터 타입 결정도 가능
- 함수 인자로도 사용 가능
'''

@app.route('/user/<userName>')
def get_uriName(userName):
    return 'user: ' + userName

# http://127.0.0.1:5000/user/gildong


# string 타입의 username 파라미터(string 타입이 default)
@app.route('/userinfo/<username>')
def show_user(username):
    return '<h1>user name is %s </h1>' %username

# http://127.0.0.1:5000/userinfo/gildong


# integer 타입 postId 파라미터
@app.route('/bbs/<int:postId>')
def show_post(postId):
    return '<h1>postID Number is %d </h1>' %postId

# http://127.0.0.1:5000/bbs/10


# float 타입 파라미터
@app.route('/circle/<float:pi>')
def show_pi(pi):
    return '<h1>pi is %f </h1>' %pi

# http://127.0.0.1:5000/circle/3.141592


if __name__ == '__main__':
    app.run()