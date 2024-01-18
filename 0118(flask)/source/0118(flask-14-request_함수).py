from flask import Flask, request

app = Flask(__name__)

'''
# request.args : GET 방식만 사용 가능

# request.values : HTTP 매서드 타입에 상관없이 데이터를 처리할 수 있는 속성

[유의]
- GET, POST 방식이 동일한 변수명을 사용할 경우 values 속성은 GET 매서드 데이터를 우선처리
'''
@app.route('/data', methods = ['GET', 'POST'])
def getValues():
    return request.values.get("name", default="전달된 데이터 없음")
# http://127.0.0.1:5000/data?name=kim
# http://127.0.0.1:5000/data


@app.route('/intData', methods = ['GET', 'POST'])
def getValues2():
    result = request.values.get('num1', "0", type = int)
    return str(result)
# http://127.0.0.1:5000/intData?num1=100
# http://127.0.0.1:5000/intData


'''
type 값으로 파이썬에서 제공하는 기본 타입 외 함수, 클래스도 사용 가능
-> 사용자 정의 데이터 타입으로 사용이 가능
'''

# 사용자 정의 함수(특정한 날짜 형식을 지정하는 함수)
from datetime import datetime
def userDateType(date_format):
    def changeFormat(date_string):
        # strptime(date_string, format) : format에 맞는 date_string을 datetime 객체로 반환
        return datetime.strptime(date_string,date_format)
    return changeFormat

@app.route('/date', methods = ['GET', 'POST'])
def getValues3():
    # print(request.values.get('date', default='2024-01-18', type=userDateType("%Y-%m-%d")))
    # return "콘솔에서 확인"
    
    time = request.values.get('date', default='2024-01-18', type=userDateType("%Y-%m-%d"))
    print(time)
    print(type(time))
    
    result = str(time)
    print(result)
    return result
# http://127.0.0.1:5000/date?date=2024-01-18

if __name__ == "__main__":
    app.run()