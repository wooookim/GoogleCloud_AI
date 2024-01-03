class Test:   # 클래스명 첫글자 대문자 권장
    str = 'This is class'    # str(변수): 클래스의 요소(필드, attribute)

test1 = Test()   # 객체화, 인스턴스화
# print(test1.str)


class Person:
    def say():   # say(함수): 클래스의 요소(매서드, attribute) # 클래스에서 생성하면 self 사용 가능
        print('oop..')
'''
일반함수와 클래스 내부의 함수(인스턴스 매서드) 차이 -> self

인스턴스 매서드의 경우 인수에 항상 self를 가장 처음 두어야 한다(없어도 인정 가능)
- def say(self, message):
    print(message)  
- 인스턴스 매서드 호출 시 self 매개변수에는 사용자(개발자)가 직접 값을 넘길 필요가 없다
'''
p1 = Person()
# p1.say()

class Person2:
    pass    # 요소를 지정하지 않으려면 pass를 반드시 작성


'''
파이썬에 존재하는 매서드
- 매서드명 앞/뒤에 '__'
- python special attribute 검색

1. init method: 클래스가 인스턴스화될 때 자동으로 호출
 - 필수적인 정보, 사전정의 정보 지정
 - 객체가 생성될 때 여러가지 초기화 작업을 하고자 할 때 유용
'''
class Person3:
    def __init__(self, name):
        self.name = name
         
    def info(self):
        print(f'이 객체의 이름은 {self.name} 입니다')
        
p2 = Person3('김성우')
p3 = Person3('김김성우')

# p2.info()
# p3.info()


'''
네임스페이스
- 클래스의 필드(클래스 내부 또는 객체화된 내부)

필드를 누가 소유하고 있는가에 따라 클래스 변수, 객체(인스턴스) 변수로 구분

클래스 변수 특성
- 클래스로부터 생성된 모든 인스턴스들이 접근할 수 있다(공유)
- 어떤 객체가 클래스 변수를 변경한다면 다른 인스턴스들에게도 변경 내용이 반영

객체 변수 특성
- 클래스로부터 생성된 각각의 객체에 속해있는 변수
- 각 객체별로 하나씩 따로 가질 수 있는 변수(공유되지 않음)
'''
class Character:
    cnt = 0  # 클래스변수
    
    def __init__(self, name):
        # 객체 데이터 초기화
        self.name = name    # self.name: 객체 변수
        print(f'{self.name} 이/가 생성중.....')
        
        # 인스턴스 매서드에서 클래스 변수 접근 -> 클래스명.클래스변수
        Character.cnt += 1
        
    def info(self):
        print('생성 완료... 내 이름은 {}'.format(self.name))
    '''
     @(at) : decorater
     - 특수한 기능을 가진 매서드로 지정
     
     classmethod -> 객체화하지 않아도 쓸 수 있게 사용  
     static      -> 객체화하지 않아도 쓸 수 있게 사용 둘 다 같은 기능
    '''
    @classmethod
    def Check(cls):
        # 현재 생성된 캐릭터 개수를 확인
        print(f'현재 생성된 캐릭터 {Character.cnt}명')
    
    '''[실습]'''
    def die(self):
        # print(f'{self.name} 캐릭터 삭제')
        # if Character.cnt >= 1:
        #     Character.cnt -= 1
        # else:
        #     Character.cnt == 0
            
        Character.cnt -= 1
        if Character.cnt == 0:
            print(f'{self.name} 마지막 캐릭터')
            # die() 매서드가 구현되지 않도록 추가할 필요가 있음
        elif Character.cnt < 0:
            Character.cnt == 0
        else:
            print('아직 {:d} 명의 캐릭터 생존'.format(Character.cnt))
            

# 객체화 없이(변수 설정없이) 클래스.매서드() 형태로 호출
# Character.Check()

'''
[실습]
die() : 캐릭터 삭제 처리

캐릭터 숫자가 음수가 되지 않도록

출력 : ~ 캐릭터 삭제
     : 캐릭터 숫자 감소
'''
# npc1 = Character('김')
# npc2 = Character('성')
# npc3 = Character('우')

# # npc3.info()

# # npc1.info()
# # Character.Check()

# Character.die('김')
# # npc1.die()
# Character.Check()


'''
상속 inheritance
'''
'''class Human():
    def eat(self):
        print('삼시세끼 챙기기')
    def sleep(self):
        print('잠자기')
    def walk(self):
        print('걷기')
    def coding(self):
        print('copy & paste')
        
class Dog():
    def eat(self):
        print('사료 먹기')
    def sleep(self):
        print('잠자기')
    def walking(self):
        print('네발로 걷기')
    def detect(self):
        print('집지키기')'''
'''
각 클래스의 공통된 속성을 그룹화

추상화
- 공유되는 부분을 만듦
- 각 클래스가 공유되는 부분을받아서 사용할 수 있도록 하는게 효율적 -> 상속

부모클래스     <-> 자식클래스
(super class) <-> (sub class)
'''
'''class Animal():
    def eat(self):
        print('음식을 먹는다')
    def sleep(self):
        print('잔다')
        
# 상속: 클래스(부모클래스)
class Human(Animal):
    def coding(self):
        print('copy & paste')
        
class Dog(Animal):
    def detect(self):
        print('집 지키기')'''

# person = Human()
# person.eat()
# person.sleep()
# person.coding()

# dog = Dog()
# dog.eat()
# dog.sleep()
# dog.detect()

'''
사람과 개는 걸을 수 있지만, 동일하게 걷지않음(로직적으로 다름)

method override
걷는다를 표현하면서 표현 방식을 달리 적용
상속을 받고 객체별로 적용시키기
'''
'''class Animal():
    def eat(self):
        print('음식을 먹는다')
    def sleep(self):
        print('잔다')
    
    # override를 위한 매서드
    def move(self):
        print('객체가 움직인다')
        
        
# 상속: 클래스(부모클래스)
class Human(Animal):
    def coding(self):
        print('copy & paste')
    # 걷는 형식
    def walk(self):
        print('두 발로 걷는다')
    
    def move(self):
        self.walk()
    
        
class Dog(Animal):
    def detect(self):
        print('집 지키기')
    # 걷는 형식
    def walking(self):
        print('네 발로 걷는다')
        
    def move(self):
        self.walking()
        
person = Human()
dog = Dog()

# person.move()
# dog.move()
# dog.walking()
'''


class Animal():
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print('음식을 먹는다')
    def sleep(self):
        print('잔다')
    
    # override를 위한 매서드
    def move(self):
        print(f'걷는 것은 {self.name}이다')
        
        
# 상속: 클래스(부모클래스)
class Human(Animal):
    def __init__(self, name):
        # 부모의 매서드를 호출: super()
        super().__init__(name)
        
    def coding(self):
        print('copy & paste')
    # 걷는 형식
    def walk(self):
        print('두 발로')
    
    def move(self):
        self.walk()
        super().move()
    
        
class Dog(Animal):
    def __init__(self, name):
        # 부모의 매서드를 호출: super()
        super().__init__(name)
        
    def detect(self):
        print('집 지키기')
    # 걷는 형식
    def walking(self):
        print('네 발로')
    
    def move(self):
        self.walking()
        super().move()

person = Human('사람')
person.move()
dog = Dog('개')
dog.move()
