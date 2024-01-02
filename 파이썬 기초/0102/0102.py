'''
야구
1. 컴퓨터 랜덤하게 세자리 정수
2. 중복 불가
3. 사용자로부터 3자리 입력
4. 자릿수별로 나눌 수 있어야 함
5. 각 자리별로 값을 비교
6. 자리와 수가 모두 같으면 스트라이크, 수는 일치하지만 자리가 다르면 볼
7. 스트라이크가 3이면 종료
'''

# import random

# com = list()
# while len(com) != 3:
#     num = random.randint(1, 9)
#     if num not in com:
#         com.append(num)    
# print(com)

# strike = 0
# ball = 0
# cnt = 0

# while strike != 3:
#     user = input('3자리 정수 입력: ')
    
#     # user_num = list()
    
#     # user_num.append(int(int(user)/100))
#     # user_num.append(int(int(user)%100/10))
#     # user_num.append(int(int(user)%10))
#     cnt += 1
#     strike = 0
#     ball = 0
    
#     for idx, val in enumerate(user):
#         # print(f'index : {idx}, value : {val}')
#         # print(type(idx), type(val))
    
#     # for idx, val in enumerate(user):
#     #     print(f'index : {idx+1}, value : {val}')
#     #     print(type(idx), type(val))
    
#         if int(val) == com[idx]:
#             strike += 1
#         elif int(val) in com:
#             ball += 1
            
#     print(f'{strike} 스트라이크, {ball} 볼')
         
# print(f'{cnt} 번')


'''
__init__.py
-> 존재 여부에 따라 (패키지 <> 디렉토리) 구별

+ 파이썬 패키지
- 관련있는 클래스와 함수들을 정도를 구분하지 않고 모듈(라이브러리) 하나에 넣는 것은 지양
- 모듈을 모으면 모두 관련이 있지만 세부적으로 나누면 그룹을 따로 둘 필요가 있음
 -> 관련성 높은 모듈들 끼리 다시 한 번 묶을 방법(개념) 필요
 
+ 파이썬 패키지 생성
-  __init__.py 파일을 디렉토리에 넣어두면 해당 디렉토리는 파이썬 패키지가 됨
 -> 모듈을 갖는 디렉토리
 
+ 패키지 호출
- 모듈 호출 방법과 동일
''' 

# 패키지 호출
# from pkg.cal import add
# print(add(1, 4))


'''
execpt

파이썬 프로그램에서 벌어지는 예외적인 상황들
파이썬은 이런 예외 상황이 벌어지면 프로그램을 중단하고 에러 메세지를 보여줌
서비스가 멈추는 단점이 생김
-> 서비스를 멈추지 않고 예외적인 상황을 처리

에러 예시)
- IndexError : 없는 인덱스를 찾을 때
- FileNotFoundError : 파일이 없을 때
- ZeroDivisionError : 숫자를 0으로 나눌 때
- SyntaxError : 문법 오류
- EOFError : end of file / 읽은 내용이 없을 때

기본구조
try:                         -> 에러가 발생하면
    <코드 블록>
execpt [발생 에러[as 별칭]]:  -> 이렇게 처리
    <수행 명령>
'''
# list1 = []
# print(list1[0]) # 에러

# text = '111111111python'
# number = int(text)
# print(number)  # 에러

# number1 = int(text[:3])
# print(number1)


# 예외 처리(코드는 그대로 두고 멈추는 상황만 예외시킴)
# text = '100%'
# num = int(text)
# print(num)

# text = '100%'
# try:
#     num = int(text)
#     print(num)
    
    # list1 = []
    # print(list1[0])
# except ValueError:
#     print(f'{text}은 숫자가 아님')
# except IndexError:
#     print(f'{text}은 숫자가 아님')
    
    
def take(list, index):
    try:
        print(list.pop(index))
        print(list)
    except IndexError:
        print(f'{index} index 번호가 없음')
        
# take([1, 2, 3], 1)
# print('-'*40)
# take([1, 2, 3], 3)
'''
의미있는 변수/함수명 설정
주석 달기
'''


'''
[실습]
take 함수 구문을 try~exception 없이 if 구문으로 처리
'''
def take2(list, index):
    if index <= len(list) - 1:
        print(list.pop(index))
        print(list)
    else:
        print(f'{index} index 번호가 없음')
        
# take2([1, 2, 3], 1)
# print('-'*40)
# take2([1, 2, 3], 3)


'''
예외 이름을 모를 때

try:
except Exception as e:
'''        
# try:
#     list2 = []
#     print(list2[0])
# except:
#     print('오류')
    
# try:
#     text = '100%'
#     number = int(text)
# except:
#     print('오류')

# try:
#     # list3 = []
#     # print(list3[0])
    
#     text = '100%'
#     number = int(text)
#     print(number)
# except Exception as e:  # 오류 사유
#     print('오류 발생:', e)   # 가장 먼저 처리되는 오류
'''
예외 활용
- 오류를 의도적으로 발생시킬 때
- 다른 코드에서 쓸 함수나 모듈 생성 시 디버깅 목적으로 오류를 일으키기

-> raise: 오류를 고의적으로 발생시키는 구문
'''
# 가위 바위 보 함수
def rsp(x, y):
    allowed = ['가위', '바위', '보']
    if x not in allowed:
        print('x는 허용되지 않는 단어')
    if y not in allowed:
        print('y는 허용되지 않는 단어')
# rsp(x = '가위', y = '묵')

def rsp2(x, y):
    allowed = ['가위', '바위', '보']
    if x not in allowed:
        raise ValueError
    if y not in allowed:
        raise ValueError    
# rsp2(x = '가위', y = '묵')
# try:
#     rsp2(x = '가위', y = '묵')
# except ValueError:
#     print('잘못된 값 입력됨')


'''
예시

KBL : 2M가 넘는 외국인 가드가 있다면 그 구단 정보를 출력하고, 활동을 멈춤
'''
kbl = {'A구단':[178, 188, 190, 198, 201],
       'B구단':[199, 192, 189, 210, 198]}

# for id, heights in kbl.items():
#     for height in heights:
#         if height > 200:
#             print(id, '2m가 넘는 선수가 있음')
#             break   # 가장 가까운 반복문에서 탈출
'''
어느 구단이던 2m가 넘는 외국인 가드가 있다면 무조건 중단
'''
# for id, heights in kbl.items():
#     for height in heights:
#         if height > 200:
#             print(id, '2m가 넘는 선수가 있음')
#             raise StopIteration
'''
[실습] 위 task를 예외처리
-> 최종출력
 A구단 2M가 넘는 선수가 있다
 규약 위반
'''
# try:
#     for id, heights in kbl.items():
#         for height in heights:
#             if height > 200:
#                 print(id, '2m가 넘는 선수가 있음')   # 여기까지 수행 후 에러
#                 raise StopIteration
# except StopIteration:
#     print('규약 위반')

'''
excepttion 다루는 방법
1. 예외 처리
2. 파이썬에 사전에 정의되어있는 예외를 일으키는 방법

코드가 길어지고 복잡해지면 함수나 로직을 여러번 호출하게 되고, 오류가 발생할 수 있는 코드도 많아짐
처리하지 말아야 할 오류를 처리해버리면 코드 전체가 달라지는 경우도 발생
(처리한 오류가 어디에서 발생하는지를 찾는 것은, 오류를 처리하지 않는 것을 찾는 것보다 더 번거롭다)

예외도 하나의 클래스로 만들어 놓고 사용자(개발자, 분석가)가 (프로젝트 별) 규정된 예외를 처리하도록 하는 경우가 많다.
'''

# '''
# 코랩 파일 생성 명령
# %%writefile <파일명.py>
# '''

'''
예외의 최상위 객체 : Exception
흔한 오류 : ValueError

상황에 맞는 오류를 정의할 것
'''
# value1 = '가'

# try:
#     if value1 not in ['A', 'B', 'C']:
#         raise ValueError('알파벳 중 하나여야 함')
# except ValueError as ve:
#     print(ve)
#     print('오류 발생')

# value2 = '가'
    
# from Except import Unecpected_exception

# try:
#     if value2 not in ['A', 'B', 'C']:
#         raise Unecpected_exception('알파벳 중 하나여야 함')
# except Unecpected_exception as ue:
#     print(ue)
#     print('오류 발생')


'''
OOP(Object Oriented Programming)
- 객체지향

프로그래밍 발전
- 순차적 프로그래밍
- 절차적 프로그래밍 -> 절차지향적 프로그래밍
- 객체지향 프로그래밍

객체를 클래스로 표현
객체는 독립적

파이썬 객체
- 클래스: 쿠키 틀
- 객체(인스턴스): 쿠키 틀로 찍어낸 각각의 쿠키

객체화(인스턴스화) = 틀로 찍는 작업
'''

'''
클래스 생성

class <클래스명>:          # 통상 클래스명은 첫글자를 대문자로 정의
    변수(필드/field)       # 클래스에 선언된 변수는 필드(field)라고 부름
    함수(매서드/method)    # 클래스에 선언된 함수는 매서드(method)라고 부름
    
필드, 매서드를 통틀어 클래스의 속성(attribute)라고 부름
'''
# 클래스 생성 시 아무런 속성이 없을 경우 반드시 pass를 작성
class Human:
    pass

# 객체화(인스턴스화)
person1 = Human()
person2 = Human()    # 독립적 = 변수가 다르면 된다 / 저장된 위치(주소)가 다르다

# print(type(person1), type(person2))
# print(type(1), type('hello'))

# 객체가 특정 클래스에 속하는지 여부 확인: isinstance()
# print(isinstance(1, float))
# print(isinstance(person1, person2))  # 에러
# print(isinstance(person1, class))  # 에러
# print(isinstance(person1, Human))  # 구체적 클래스명으로 비교
# print(person1 == person2)  # False
# print(person1, '-', person2)
'''
프로젝트 규모가 커지면서 클래스 활용도가 높아짐
'''

'''
# 객체에 특성(성질)을 주입 = 값을 대입
person1.language = 'KOREAN'
person2.language = 'AMERICAN'
# print(person1.language, person2.language)

person1.name = '김성우'
person2.name = '데귤'
# print(person1.name, person2.name)

# 객체이므로 함수(행위)도 부여 가능
def speak(person):
    print('{}님이 {}로 연설합니다.'.format(person.name, person.language))
# speak(person1)
Human.speak = speak
# speak(person1)
# speak(person2)

위 처럼 사용하면 객체 안에 즉, 객체가 함수를 적용한 것이 아님
-> 일반 함수를 사용하는 형태로 구현됨

클래스 안에 함수를 적용하려면 행위 자체도 인스턴스화되어야 한다
'''
# 객체화(인스턴스화)
person3 = Human()

person3.name = '데귤데귤'
person3.height = '100'

# print(person3, person3.name, person3.height)
'''
객체를 생성할때마다 데이터를 초기화하는 것은 비효율적이다
함수로 만들어 놓고 인스턴스를 생성 - 이때 함수를 "생성자"
'''
def create_human(name, height):
    person = Human()
    person.name = name
    person.height = height
    return person

# Human 클래스에 매서드 지정
Human.create = create_human

# 객체 실체화 => 모델링
person4 = Human.create('귤귤', 111)
# print(person4, person4.name, person4.height)

'''
비어있는 클래스와 일반함수를 따로 만들고,
일반함수를 비어있는 클래스의 내부 함수(매서드)로 대입하는 방식은 문제가 있음
-> 클래스 안에 속성을 미리 저장해두는 것을 권장
'''

class Indivisual():   #() 붙여도 됨
    pass

    # 인스턴스를 생성 및 초기화하는 함수
    def create_human(name, height):
        person = Indivisual()
        person.name = name
        person.height = height
        return person
    
    # 새로운 행위
    def eat(person):
        person.height += 0.3
        print('{}가 먹어서 키가 {}가 되었다'.format(person.name, person.height))
        
    # 새로운 행위2
    def walk(person):
        person.height += 0.1
        print('{}가 걸어서 키가 {}가 되었다'.format(person.name, person.height))

    # self
    # def sleep(self, a, b):
        
person5 = Indivisual.create_human('성우', 177)  # 초기화
person5.eat()   # 매개변수를 입력하는 대신 person5가 매개변수로 작동 -> 객체가 작동(매개변수가 비어있음)
'''
행위가 클래스(객체) 중심일 때는 이 객체가 수행한 것이므로 굳이 인자(매개변수)로 전달해줄 필요가 없음

매서드가 가진 규칙
1. 매서드 호출 시 첫번째 인자를 생략하면 인스턴스 자신으로 채움
 - keyword: self
'''
