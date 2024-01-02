'''
예외의 최상위 객체 : Exception
흔한 오류 : ValueError

상황에 맞는 오류를 정의할 것
'''
class Unecpected_exception(Exception):
    print('new exception')