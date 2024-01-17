from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def get_page():
    return render_template('sub_01.html',  str = '템플릿 상속 페이지', arr = [11, 22, 33, 44, 55])

if __name__ == '__main__':
    app.run(debug=True)
    