from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello flask world</h1>'

@app.route('/user/<userid>')
def user(userid):
    return render_template('user.html', name = userid)

# http://127.0.0.1:5000/user/kimsw

if __name__ == '__main__':
    app.run(debug=True)