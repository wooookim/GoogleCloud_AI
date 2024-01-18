'''
session : 웹 사이트 여러 페이지에 걸쳐 사용되는 사용자 정보를 저장하는 방법
-> 사용자가 브라우저를 닫아서 웹 서버와의 연결을 끝내는 지점까지

쿠키는 클라이언트에 저장(보안 상 위험)  <>  세션은 웹서버에 저장

공통점
- 웹 통신 간 유지하려는 정보를 저장하기 위해 사용하는 객체

차이점(쿠키 <> 세션)
- 저장위치(클라이언트 브라우저 <> 웹 서버)
- 저장형식(Text <> Object)
- 만료시점(설정 가능 <> 브라우저 종료 시)
- 사용자원(클라이언트 <> 웹 서버)
- 용량(300개(도메인 당 20개, 쿠키 당 4KB) <> 웹 서버 허용 수준)
- 속도(쿠키 > 세션)
- 보안(cookie < session)

about flask's session keys
- SECRETE_KEY : 비밀 키 설정
- SESSION_COOKIE_NAME: 세션 쿠키 설정, default 'session'
- PERMANENT_SESSION_LIFETIME : 세션 유효기간 설정, default 31일
'''

from flask import Flask,request,session
app = Flask(__name__)

app.secret_key = 'secretkey123!'

# session 설정 / 삭제
@app.route('/session')
def setSession():
    session['ID'] = 'Flask Session'
    return 'desig session'

@app.route('/session_out')
def outSession():
    del session['ID']
    return '세션 제거'


if __name__ == '__main__':
    app.run()