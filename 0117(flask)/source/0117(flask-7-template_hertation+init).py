'''
템플릿 상속

- {% extends '부모 템플릿 이름'%}

- {% block %} 대체 코드 {% endblock %}
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def get_page():
    return render_template('sub_init.html', str = '템플릿 상속 테스트', arr = [11, 22, 33, 44, 55])



if __name__ == '__main__':
    app.run(debug=True)