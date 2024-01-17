from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # 경로 지정 없으면 함수에 매개변수 불필요
def template_test(): # 경로 지정 없으면 함수에 매개변수 불필요
    return render_template('expression.html', str = '템플릿 테스트', array = [11, 22, 33, 44, 55], asdfasdfa = 1)    # html에 리스트 인덱싱 사용 가능, 아무변수나 사용 가능

'''
서버가 구동되면 클라이언트에게 보여줄 화면에 출력
[출력]
div.container
    h1 this is ~
    
    ul li 11
          22
          33
          44
          55
'''


if __name__ == '__main__':
    app.run(debug=True)