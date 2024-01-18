'''
쿠키
- 웹 브라우저에 존재하는 정보 조각 -> db용량 간소화를 위해 클라이언트가 정보를 갖고 접근
- 기본구성: 쿠키명 - 쿠키값
- 특성
    1. 정해진 시간 동안 유지(권장)
    2. 지정된 웹 사이트 경로에 영향을 미침
    3. 지정된 도메인 주소에도 영향을 미침

-> set_cookie() 매개변수
    1. key     : 쿠키 이름(쿠키 설정시 필수 지정)
    2. value   : 쿠키 값(default : 빈 문자열)
    3. max_age : 쿠키 지속 시간(default : None -> 브라우저가 닫히면 쿠키 제거)
        * 시간 단위는 초(sec)단위 설정 -> 이후 쿠키가 자동 삭제
    4. domain  : 쿠키의 영향력이 미치는 도메인 주소(기본값 = None)
    5. path    : 쿠키의 영향력이 미치는 웹 사이트 상 경로(기본값 = '/')
'''

# 쿠키 생성/확인/삭제
from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/cookie_set')
def setCookie():
    res = Response('쿠키 객체 생성 중')
    res.set_cookie('cookieName', 'hello cookie')
    return res

@app.route('/cookie_status')
def statusCookie():
    return 'cookieName 쿠키는 %s 값을 갖고 있다' %request.cookies.get('cookieName')

@app.route('/cookie_out')
def outCookie():
    res = Response('쿠키 삭제')
    res.set_cookie('cookieName', expires = 0)  # 지속시간을 0으로 처리해서 삭제
    return res

if __name__ == '__main__':
    app.run()