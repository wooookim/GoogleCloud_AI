from flask import Flask

app = Flask(__name__)

# View(view함수)
@app.route('/hello/')   # 주소 표기 시 '/' 유의
def hello_flask():
    return "Hello Flask"

if __name__ == '__main__':
    app.run()