'''
flask에서 웹 브라우저에 응답할 때 모든 데이터는 Response 객체를 이용한다

Response 객체를 생성할 때 사용하는 매개변수
- response : 웹 브라우저에게 응답할 데이터
- status   : HTTP 상태코드
- header   : 웹 브라우저에게 응답할 header(메타 정보)
- minetype : image/jpeg, text/html과 같이 HTTP 메세지 바디가 어떤 MINE type 데이터인지를 지정
- content_type : (= minetype)

Response 객체에서 HTTP 메세지 바디와 쿠키를 설정하는 매서드
- get_data : 브라우저에 응답할 데이터를 반환(data 속성에 있는 값을 얻을 때)
- set_data : 브라우저에 응답할 데이터를 변경
- set_cookie : 클라이언트 쿠키를 설정
'''
from flask import Flask, Response
app = Flask(__name__)

@app.route('/')
def res():
    res = Response('응답 테스트')
    
    # res.headers.add('WebApp-Name', 'Flask-Response')
    res.set_data('플라스크 응답 객체 확인')   # 브라우저 제어
    
    return res
    
if __name__ == '__main__':
    app.run()