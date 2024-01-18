'''
templates - html
static - css - register.css
static - js - .js
'''
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/register/', methods = ['GET', 'POST'])
def practice():
    return render_template('register.html')

# userid=123&pwd1=123&pwd2=123&level=샛별&fullname=12345&email=123%40123.com&tel=123&skill=2


@app.route('/register/id')
def getRequest():
    res = "{}".format(request.args.get('userid'))
    return res



if __name__ == '__main__':
    app.run()