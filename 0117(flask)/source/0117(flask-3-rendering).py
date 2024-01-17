from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('demo.html')

if __name__ == '__main__':
    app.run()


'''
[주의]
실행 파일과 같은 층위에 templates 폴더를 만들고 그 폴더 내에 html파일 배치
'''