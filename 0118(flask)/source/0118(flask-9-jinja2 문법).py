'''
jinja2 tempalte engine 문법, 함수
'''
from jinja2 import Environment, FileSystemLoader

# template 파일이 있는 디렉토리 호출
file_loader = FileSystemLoader('C:/Users/user/gcp/0118(flask)/source/templates')

# 환경 호출
env = Environment(loader = file_loader)


template9 = env.get_template('whiteSpace.html')
print(template9.render(boolean = False))