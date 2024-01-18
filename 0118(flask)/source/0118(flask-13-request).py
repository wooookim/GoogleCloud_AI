'''
HTTP 메시지(request / response)

flask에서 http요청/응답을 처리하기 위해서 request 객체, response 객체를 사용
- flask 모듈에서 호출 후 사용
'''

from flask import Flask, request

app = Flask(__name__)

# GET 데이터 가져오기
@app.route('/data')
def getRequest():
    return "request 객체를 이용해서 주소창으로부터 얻어온변수 name 값은 {}".format(request.args.get('name'))  # ?이하 
# http://127.0.0.1:5000/data?name=kim
# request에 있는 args는 GET 방식만 접근 가능


# HTTP메세지는 웹서버와 웹브라우저 간 문자열 타입으로만 데이터를 주고 받는다.
# 변수와 데이터 타입 모두 지정 가능

@app.route('/intData')
def getRequest2():
    num1Value = request.args.get('num1', '0', int)  # args.get(변수명, default, datatype)
    
    result = num1Value + 200
    
    return str(result)  # 문자열로 변환해서 반환
# 데이터를 INT(정수화)해서 송출해보면 에러화면이 출력됨
# http://127.0.0.1:5000/intData?num1=100

if __name__ == '__main__':
    app.run()