# 객체지향의 캡슐화, 추상화, 상속, 다형성 개념
# 모델링 : 사물을 분석하여 필요한 속성과 동작을 추출하는 것
# 캡슐화 : 모델링된 결과를 클래스로 포장하는 것


# 계좌 캡슐화

# balance = 8000

# deposit : 예금 입출금
# def deposit(money):
#     global balance
#     balance += money

# 예금 조회
# def inquire():
#     print('잔액은 %d원입니다.' %balance)

# deposit(1000)
# inquire()


# 계좌 클래스로 캡슐화하기

class Account:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, money):
        self.balance += money
    def inquire(self):
        print('잔액은 %d원입니다.' %self.balance)


# sinhan = Account(8000)
# sinhan.deposit(1000)
# sinhan.inquire()

# nonghyup = Account(1200000)
# nonghyup.inquire()

# 사물의 속성은 변수로 표현
# 동작은 함수로 표현 -> 클래스로 캡슐화
# 클래스를 구성(변수 + 함수 = 멤버)
# 메서드 : 클래스에 소속된 함수

# 생성자
# 클래스는 첫 자를 대문자로 적는것이 관행
# class 이름 :
#     def __init__(self, 초기값):
#         멤버 초기화
#     메서드 정의

# __init__ : 객체 초기화
# 메서드의 첫 번째 인수는 자기 자신을 의미하는 self
# 나머지 인수로 멤버의 초기값을 대입

# class Human:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
        
#     def intro(self):
#         print(str(self.age) + '살' + self.name + '입니다.')


# cho = Human(37, '조을연')
# jang = Human(31, '장한솔')

# cho.intro()
# jang.intro()

# 객체를 선언할 때마다 새로운 기억장소가 할당되고 생성자에서 각자의 초기값을 대입
# Human으로부터 만들어진 cho, jang은 객체, 고유한 멤버값을 유지
# 인스턴스 : 클래스로부터 생성된 각각의 객체


# 상속 : 기존 클래스를 확장하여 멤버를 추가하거나 동작을 변경
# Human 상속
# class Student(Human):
#     def __init__(self, age, name, stunum):
#         super().__init__(age, name)
#         self.stunum = stunum

#     # def intro(self):
#     #     super().intro()
#     #     print('학번 : ' + str(self.stunum))

#     def intro(self):
#         print('%d학번 %s입니다.'%(self.stunum, self.name))  # override 예시

#     def study(self):
#         print('눈누난나')

# cho.intro()
# jang = Student(31,'장한솔', 1012393)
# jang.intro()
# jang.study()

# 자식 클래스에서 부모의 매서드를 호출할 떄는 super() 메서드 사용
# 자식은 부모의 모든 메서드를 물려받음
# override : 같은 이름의 메서드를 재정의하여 부모의 동작을 원하는 대로 수정


### 엑세서
# 객체가 부품으로서의 안정성을 확보하려면 외부의 부주의한 사용으로부터 자기 자신을 방어해야 함
# -> 정보 은폐 기능
# 파이썬은 공식적으로 정보 은폐를 지원하지 않음
# 멤버를 외부에서 조작할 수 없도록 일정한 규칙을 마련하고 안전하게 엑세스하도록 해야 함
# Getter : 멤버 값을 대신 읽어 줌
# Setter : 멤버 값을 변경

# class Date:
#     def __init__(self, month):
#         self.month = month

#     def getmonth(self):
#         return self.month

#     def setmonth(self, month):
#         if 1 <= month <= 12:
#             self.month = month

# today = Date(8)
# today.setmonth(15)
# print(today.getmonth())

# property(getter, setter) 방식

# class Date:
#     def __init__(self, month):
#         self.month = month

#     def getmonth(self):
#         return self.inner_month
    
#     def setmonth(self, month):
#         if 1<= month <=12:
#             self.inner_month = month
    
#     month = property(getmonth, setmonth)

# today = Date(8)
# today.month = 15
# print(today.month)


# 데코레이터로 프로퍼티 정의
# class Date:
#     def __init__(self, month):
#         self.inner_month = month

#     @property
#     def month(self):
#         return self.inner_month
        
#     @month.setter
#     def month(self, month):
#         if 1 <= month <= 12:
#             self.inner_month = month

# today = Date(8)
# today.month = 15
# print(today.month)


# __month로 이름을 바꿈으로 값 변경을 막음

# class Date:
#     def __init__(self, month):
#         self.__month = month

#     def getmonth(self):
#         return self.__month

#     def setmonth(self, month):
#         if 1 <= month <= 12:
#             self.__month = month
#     month = property(getmonth, setmonth)

# today = Date(8)
# today.__month = 15
# print(today.month)



# 클래스 메서드
# 클래스 전체가 공유하는 메서드
# 함수 앞에 @ 데코레이터를 붙이고 첫 번째 인수로 cls 인수를 받아들임

# class Car:
#     count = 0
#     def __init__(self, name):
#         self.name = name
#         Car.count += 1

#     @classmethod
#     def outcount(cls):  # Car 클래스 소속
#         print(cls.count)

# pride = Car('프라이드')
# korando = Car('코란도')
# Car.outcount()
# print(pride.count)   # 2 -> 이때의 pride는 객체가 아닌, 객체가 소속된 클래스를 의미
# print(korando.count) # 2 -> count는 특정 객체 소속이 아닌 클래스 소속이므로 외부에서는 Car.count형식으로 참조하는것이 원칙


# 정적 메서드
# 클래스에 포함되는 유틸리티 메서드. 특정 객체에 소속되지 않고 클래스와 관련된 동작을 하는 것도 아님
# self나 cls를 인수로 받지 않음
# 정의할 때 @staticmethod 데코레이터를 붙임

class Car:
    @staticmethod
    def hello():
        print('오늘도 안전 운행하자오')
    
    count = 0

    def __init__(self, name):
        self.name = name
        Car.count += 1

    @classmethod
    def outcount(cls):
        print(cls.count)

# Car.hello()


# 연산자 메소드
# class Human:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name

#     def __eq__(self, other):
#         return self.age == other.age and self.name == other.name

# cho = Human(37, '조을연')
# jang = Human(31, '장한솔')
# han = Human(31, '장한솔') 
# print(cho == han)  # False
# print(jang == han) # True   


# 특수 메서드
# 특정한 구문에 객체가 사용될 때 미리 약속된 작업을 수행
# __str__ : str(객체)형식으로 객체를 문자열화한다
# __repre__ : repr(객체)형식으로 객체의 표현식을 만든다
# __len__ : len(객체)형식으로 객체의 길이를 조사한다

# __str__ 이 함수를 정의해 두면 print의 인수로 객체 자체를 넘길 수 있음
# class Human:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name

#     def __str__(self):
#         return '이름 %s, 나이 %d' %(self.name, self.age)

# jang = Human(31, '장한솔')
# print(jang)



# 유틸리티 클래스
# f = 0.1
# sum = 0
# for i in range(100):
#     sum += f
# print(sum) # 9.99999999999998

# 오차 없이 정확하게 10진 실수를 표현하는 Decimal 클래스
# Decimal : 정수로 초기화하거나 '0.1' 형태의 문자열 실수로 초기화

# Decimal(123)
# Decimal('3.14')
# Decimal('3.14e3')
# Decimal((0,(3,1,4),-2))

from decimal import *

f = Decimal('0.1')
sum = 0
for i in range(100):
    sum += f
print(sum)

# decimal은 실수형과는 연산할 수 없음

# context 객체 : 연산을 수행하는 방법 지정
# 정확도와 지수의 범위, 반올림 방법, 예외 상황등

a = Decimal('11111111111')
b = Decimal('11111111111')

setcontext(BasicContext)
c = a * b
# print(c) # 1.23456790E+20

setcontext(DefaultContext)
c = a * b
# print(c) # 123456790120987654321


# Fraction
# 유리수를 표현
# Fraction([부호] 분자, 분모)
# 분자, 분모의 공배수가 있으면 약분하여 간단하게 표현

from fractions import *

a = Fraction(1,3)
print(a)

b = Fraction(8, 14)
print(b)

# Fraction 객체끼리 연산 가능. 정수, 실수 등과 연산 할 수 있음. 이때는 실수형으로 바뀜
a = Fraction(2,3)
b = Fraction(3,5)
c = a + b
print(c) # 19/15

d = c + 0.1
print(d) # 1.3666666666666667


# array
# array(타입코드, [초기값])
# array('i', range(5,10))
# array('i', [10, 89, 128])

import array

ar = array.array('i', [33,44,67,89,56])

for a in ar:
    print (a, end=',')
ar.append(100)
del ar[0]
print('\nar[1] = ', ar[1])
print(ar[2:4])
