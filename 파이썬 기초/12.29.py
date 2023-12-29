"""
comprehension
조건 제시법: 원하는 구성요소를 하나씩 집어넣는 대신 코드화해서 리스트나 딕셔너리를 바로 생성하는 방법
구조
-> [(반복실행문) for (반복변수) in (반복범위)] : list comprehension
-> {(반복실행문) for (반복변수) in (반복범위)} : dict comprehension
"""
# 정사각형 넓이
area1 = []
for i in range(1, 11):
    area1 += [i**2]
# print(area1)

area2 = [i**2 for i in range(1, 11)]
# print(area2)


"""
comprehension 확장
특정 조건을 만족하는 리스트 생성
"""
# 한변의 길이가 짝수인 정사각형의 넓이
area3 = []
for i in range(1, 11):
    if i % 2 == 0:
        area3 += [i**2]
# print(area3)

area4 = [i**2 for i in range(1, 11) if i % 2 == 0]
# print(area4)

"""
실습
list comprehension으로 1부터 100사이에 있는 8의 배수를 리스트로 출력
"""
clist = [i * 8 for i in range(1, 101) if i * 8 < 101]
clist2 = [i for i in range(1, 101) if i % 8 == 0]
# print(clist)
# print(clist2)


# 15*15 사이즈 바둑판 좌표를 튜플
# print([(x, y) for x in range(15) for y in range(15)])

"""
comprehension 유의점
반드시 for문으로 시작하고 뒤에 if문
for - if 구문을 반복 사용 가능하지만 권장하지 않음
간단한 조건일때만 중첩된 comprehension을 사용하고 통상 for문을 여러번 풀어서 사용을 권장
"""


# 사람들이 번호 순으로 있다는 가정 하 리스트 생성
peoples = ["a", "b", "c", "d", "e"]
# 위 리스트를 이용해 번호를 키로 하고 이름을 값으로 하는 딕셔너리 생성
# for num, name in enumerate(peoples):
#     print(f"{num + 1} 번째 이름은 {name}입니다")

result = {(num + 1, name) for num, name in enumerate(peoples)}
# print(result)

"""
리스트를 딕셔너리로 : zip()
"""
age = [10, 11, 12, 13, 14]

# for x, y in zip(peoples, age):
#     print(x, y)

# print({x: y for x, y in zip(peoples, age)})


"""
함수
코드 중복을 피하는 것이 목표
구조

def 함수명(입력변수):
    <코드 블록>
"""


def function():
    print("hello function")


# function()

# 입력값이 없는 함수 = 인자(인자, 매개변수)가 없는 함수
# 출력값이 고정됨
num1 = 10
num2 = 20


def sum():
    result = num1 + num2
    print(result)


# sum()


# 호출 시 입력값이 있는 함수 = 인자(인자, 매개변수)가 있는 함수
def sum2(num1, num2):
    result = num1 + num2
    print(result)


# sum2(10, 11)


"""
결과 값이 있는 함수 (keyword : return)
구조

def 함수명(<입력인수>):
    <코드블록>
    return 결과값
"""


# 결과값이 있고 매개변수는 없는 함수
def hello():
    str1 = "hi python function"
    return str1


# print(hello())

# hello = hello()
# print(hello, type(hello))


# 결과값이 있고 매개변수도 있는 함수
def add(x, y):
    result = x + y
    return result


# print(add(1, 3))


# 파라미터 입력(초기값 설정)
def add2(x, y=0):
    return x + y


# print(add2(11, 3))
# print(add2(11))


# 파라미터는 갯수와 순서는 함수와 호출 시 서로 일치
# print(add(1, 1, 1))
def add3(x, y):
    result = x + y
    return result


# print(add3(1, 1))
# 파라미터가 많아지면 이름을 명시(권장) -> 순서가 바뀌어도 괜찮아짐
# print(add3(y=10, x=2))

"""
실습
5천만원 연봉 신입사원의 연봉을 10% 인상한 값으로 돌려주는 함수 생성
"""


def upsal(x):
    result = x + x * (0.1)
    return result


# print(upsal(50000000))


"""
추가로 해본거

1억을 넘으려면 몇년 걸릴까
"""


def upsal2(x, count=0):
    result = x + x * 0.1
    if result < 100000000:
        count += 1
        return upsal2(result, count)
    else:
        return count


# print(upsal2(50000000))


"""
return
-> 오직 한 개의 결과값만 반환
-> 어떤 상황이 되어서 함수를 빠자나가고자 할 때 사용
"""


def return_keyword():
    for i in range(100):
        return i


# print(return_keyword())


# return에 결과가 없으면 아무값도 반환되지 않고 함수 탈출
def avoid(number):
    if number == 5:
        return
    print(number)


# avoid(5)


"""
함수 호출 시 입력값이 몇 개인지 모를 경우 = 가변인자

def 함수명(*입력변수명):
    <코드블록>
    return 결과값
"""


# 덧셈 함수(클라이언트가 입력한 숫자까지)
def sum3(*args):  # args = 관례적으로 사용하는 변수명
    temp = 0
    for i in args:
        temp += i
    return temp


# print(sum3(1, 3, 4, 5, 87, 6, 6))

# list1 = [1, 2, 3, 4, 5]
# # print(sum3(list1))

# tup1 = (1, 2, 3, 4, 5)
# print(sum3(tup1))


"""
key - value도 가변인자 **로 가능
"""


def priDict(**args):
    print(type(args))

    name = args["name"]
    age = args["age"]

    print(f"{name} 은 {age}세")


data = {"name": "a", "age": 27}

# priDict(**data)


"""
type annotation(type hinting)
- 기본적으로 역할을 하는게 아닌 가이드 제공
- 팀 프로젝트에서 유용
"""


# 두 갓의 차이를 구하는 함수
def sub(x: int, y: int) -> int:
    return x - y


# print(sub(10, 5.5))  # 결과는 나옴


"""
함수(파라미터, 변수)의 범위(scope)
- 함수 내부에서 선언된 변수는 외부에서 사용이 불가
"""
var = 1  # 전역변수


def scope_function(var):
    var = var + 1
    print(var)


# scope_function(var)


"""
모듈
- 동일한 목적, 비슷한 역할을 하는 함수나 변수 또는 클래스를 모아놓은 파일
- 특정 기능들(함수, 변수 등)이 구성되어 있는 파이썬 파일
- 다른 파이썬 파일(프로그램)에서 호출해 사용할 수 있게 만들어 놓은 파일

import
"""
# import calculater as cal

# print(cal.cadd(1, 2))


# from calculater import cadd

# print(cadd(3, 4))


"""
라이브러리
- 프로그램(모듈)을 모아둔 것
- 표준 라이브러리 : 파이썬과 동시에 설치되는 라이브러리
"""
import sys

# print(sys.argv)  # 수행되는 파일
# print(sys.path)  # 파일 위치

import os

# print(os.environ)  # 시스템 환경 변수


"""
1. 로또번호 6개 랜덤하게 추출

2. 야구 게임 구현
 1. 랜덤하게 숫자 3개 생성
 2. 중복 불가
 3. 숫자 3개 입력
 4. 각 자리별 값 비교
 5. 자리와 수가 같으면 스트라이크, 일지하지만 자리가 다르면 볼
 6. 3s가 나오면 종료
"""

import random

lotto_list = [i for i in range(1, 46)]
selected_numbers = random.sample(lotto_list, 6)

# print(selected_numbers)


import random


def generate_random_number():
    return random.sample(range(1, 10), 3)


def check_guess(secret, guess):
    strikes = 0
    balls = 0

    for i in range(3):
        if guess[i] == secret[i]:
            strikes += 1
        elif guess[i] in secret:
            balls += 1

    return strikes, balls


def baseball_game():
    secret_number = generate_random_number()
    attempts = 0

    print("야구 게임을 시작합니다!")

    while True:
        user_input = input("숫자 3개를 입력하세요 (1에서 9까지, 중복 없이): ")

        if len(user_input) != 3 or not user_input.isdigit():
            print("올바른 형식으로 입력하세요.")
            continue

        user_guess = [int(num) for num in user_input]

        if len(set(user_guess)) < 3:
            print("중복된 숫자를 입력하셨습니다. 다시 입력하세요.")
            continue

        attempts += 1
        strikes, balls = check_guess(secret_number, user_guess)

        print(f"결과: {strikes} 스트라이크, {balls} 볼")

        if strikes == 3:
            print(f"축하합니다! {attempts}번만에 정답을 맞추셨습니다.")
            break


baseball_game()
