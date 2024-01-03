'''
1. GuGuDan 클래스 정의
 dan = GuGuDan()
 dan.print(3)

[출력]
3x1=3
3x2=3
3x3=3
3x4=3
...
3x9=27
'''
class GuGuDan():
    def print(self, num):
        for i in range(1, 10):
            print(num,'x',i,'=',i*num)

dan = GuGuDan()
# dan.print(3)

'''
2. Calculator 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메서드를 추가

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
-----------------------------
cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value) 
'''
'''
class Calculator:
    def __init__(self):
        self.value = 0
        
    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
'''
# print(cal.value)


'''
3. 객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스 생성. 
단 반드시 다음과 같은 Calculator 클래스를 상속해서 만들기

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60) 

print(cal.value) 
-----------------------------
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
'''
class Calculator:
    def __init__(self):
        self.value = 0
        
    def add(self, val):
        self.value += val
        
class MaxLimitCalculator(Calculator):
    def add(self, val):
        super().add(val)
        if self.value > 100:
            self.value = 99
            
    
cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)