'''
HTTP 매서드
- GET / POST 가 대표적
- 외에도 PUT / DELETE / HEAD / OPTIONS... 등이 더 존재, 이러한 타입은 통상 REST API 개발 시 사용
'''
from flask import Flask
app = Flask(__name__)

# methods 매개변수로 방식 지정 / GET이 기본값
@app.route('/a_url', methods = ['GET'])
def getMethod():
    pass

@app.route('/b_url', methods = ['POST'])
def postMethod():
    pass

# http 매서드 타입에 따라서 뷰 함수가 다른 경우

# ----------------------------------------------------------

# http 매서드 타입이 달라도 뷰 함수를 하나로 사용하는경우

# 매서드에 따라 페이지를 변경할 필요 없음
@app.route('/c_url', methods = ['GET', 'POST'])
def getPostMethod():
    pass

# url 변수에 기본값 할당 가능
@app.route('/d_url', default = {'page' : 'index'})
@app.route('/d_url/<page>')  # -> http://localhost/d_url/index
def getd():
    pass