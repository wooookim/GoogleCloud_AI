'''
jinja2 템플릿 엔진
- flask 설치 시 포함되어있음
- flask를 통해 만드는 템플릿 파일(html 등)들은 기본적으로 templates 폴더에 저장

jinja2 템플릿 표현식
- {% : 템플릿에서 프로그래밍 영역(제어문 등)을 넣기 위해 시작하는 기호(block_start_string)
- %} : 프로그래밍 영역의 기술을 끝내고 프로그래밍 영역 종료하는 기호(block_end_string)

- {{ : 변수를 출력하기 위해 시작하는 기호(variable_start_string)
- }} : 변수 출력이 끝났을 때 사용하는 기호(variable_end_string)

- {# : 주석 시작(comment_start_string)
- #} : 주석 종료(comment_end_string)
'''
from jinja2 import Template

template1 = Template('hello {{name}}')
print(template1.render(name = 'kim'))

template2 = Template('number: {% for i in range(1, 10) %} {{i}} {% endfor %}')
print(template2.render())