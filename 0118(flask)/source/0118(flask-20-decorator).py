'''
HTTP 요청 전/후에 대한 핸들링

Flask에서는 핸들링을 위해 데코레이터(@) 제공
'''
from flask import Flask

app = Flask(__name__)

# @app.route('/')
# def index():
#     return '/'

@app.before_request
def before_request():
    print('매번 HTTP 요청이 처리되기 전에 실행')
    
@app.after_request
def after_request(response):
    print('매번 HTTP 요청이 처리된 후에 실행')
    
@app.teardown_request
def teardown_request(exception):
    print('매번 HTTP 요청의 모든 결과가 브라우제어 보내진 다음(모든 과정이 처리된 후) 실행')  # 세세한 흐름제어
    
@app.teardown_appcontext
def teardown_appcontext(exception):
    print('HTTP 요청의 애플리케이션 컨텍스트가 종료될 때 실행')
    
    
# route 데코레이션 대신 사용하는 매서드 : add_url_rule()
'''
@app.route('/')
def index():
    return '/'
'''
def index():
    return 'hello flask route function'

app.add_url_rule('/','index', index)   # 경로, 이름(임의지정), 함수(view function)
    

    
    
    
    
    
if __name__ == '__main__':
    app.run()
