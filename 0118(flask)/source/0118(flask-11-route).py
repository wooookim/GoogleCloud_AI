from flask import Flask

app = Flask(__name__)

# @app.route('/bbs/<bbs_id>')
@app.route('/bbs', defaults = {'bbs_id': 0})  # 기본값 지정
def rules(bbs_id):
    return 'bbs의 {}번째 내용'.format(bbs_id)
    # return f'bbs의 {bbs_id}번째 내용'

# http://127.0.0.1:5000/bbs/10
# http://127.0.0.1:5000/bbs


if __name__ == '__main__':
    app.run()
