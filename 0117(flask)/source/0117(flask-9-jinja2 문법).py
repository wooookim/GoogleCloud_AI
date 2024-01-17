'''
jinja2 tempalte engine 문법, 함수
'''
from jinja2 import Environment, FileSystemLoader

# template 파일이 있는 디렉토리 호출
file_loader = FileSystemLoader('C:/Users/user/gcp/0117(flask)/source/templates')

# 환경 호출
env = Environment(loader = file_loader)

# 텍스트 파일도 렌더링 가능
template = env.get_template('helloworld.txt')
print(template.render())
print('-'*30)

template2 = env.get_template('dogs.txt')
print(template2.render())
print('-'*30)

# jinja2 변수 지정 문법도 그대로 텍스트 파일을 이용해 렌더링
template3 = env.get_template('dogs.txt')
print(template3.render(name = 'simdang', species = '풍산개'))
print('-'*30)

# 객체에 대한 접근도 가능
template4 = env.get_template('personInfo.txt')
person = {}
person['name'] = '율곡이이'
person['salary'] = 1000
print(template4.render(data = person))
print('-'*30)
'''
[실습]
율곡이이는 급여를 10000만원 받습니다
 출력
'''

# 논리값도 가능
template5 = env.get_template('ifStructure.txt')
# print(template5.render(bool = False))
print(template5.render(truth = False))
print('-'*30)

# 리스트도 가능
template6 = env.get_template('forColor.txt')
colors = ['r', 'g', 'b']
print(template6.render(rainbow = colors))
print('-'*30)

# include 형식 - HTML에서 많이 사용
# header.html 파일을 base.html에 삽입
template7 = env.get_template('base.html')
print(template7.render(title = 'include 된 페이지 title'))

# header.html을 삽입한 base.html을 child.html에 상속
template8 = env.get_template('child.html')
print(template8.render(title = 'include 된 페이지 title', body = '상속 body'))