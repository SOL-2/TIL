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


sinhan = Account(8000)
sinhan.deposit(1000)
sinhan.inquire()

nonghyup = Account(1200000)
nonghyup.inquire()