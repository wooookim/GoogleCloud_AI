from flask import Flask

# 플라스크 객체 생성 / __name__ : 현재 실행 중인 모듈 이름을 전달
app = Flask(__name__)

# 기본 서버주소(http://127.0.0.1:5000) 뒤 주소 지정
@app.route('/')
# 위 주소를 호출 시 클라이언트에게 보여줄 내용을 담는 함수(중복 불가)
def index():
    return "hello flask world v2"

if __name__ == '__main__':
    app.run(debug=True, port=9090)
    
# flask 실행하는 파일 이름을 flask.py로 하는 것을 권장하지 않음