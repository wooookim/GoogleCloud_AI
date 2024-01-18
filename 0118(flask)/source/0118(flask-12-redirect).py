from flask import Flask

app = Flask(__name__)

'''
# redirect_to
# url 전달

@app.route('/index', redirect_to = '/new_index')
def index():
    return "/index 주소로 호출된 페이지"

@app.route('/new_index')
def new_index():
    return "/index 에서 바로 /new_index로 호출한 페이지"
'''

'''
# redirect_to option
# 함수 전달
    - 사전에 함수 정의
    - 정의된 함수 첫번째 인자는 필수적으로 adapter
    
    처음 요청 시 수신했던 파라미터를 그대로 redirect 되는 페이지에 넘겨줄 수 있다
    
    * 동일한 수의 url 인자를 기술
'''
# 데이터를 보내는 함수
def redirect_fowarding_function(adapter, p1, p2):
    return '/new_index/{0}/{1}'.format(p1, p2)

@app.route('/index/<p1>/<p2>', redirect_to = redirect_fowarding_function)
def index():
    return "/index/p1/p2 로 호출되는 페이지"

@app.route('/new_index/<p1>/<p2>')
def new_index(p1, p2):
    return "/new_index/{0}/{1} 으로 호출되는 페이지".format(p1, p2)

if __name__ == '__main__':
    app.run()