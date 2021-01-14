# age = int(input('몇 살이신가요? : '))
# if age >= 30:
#     print('계란 한판을 넘었다!!!!!')


# num = int(input('10 이상의 숫자를 입력하세요 : '))

# if num == 10:
#     print('10이다')

# if num > 10:
#     print('10보다 크다')

# if num < 10:
#     print('엥?? 멍청이냐오 ㅋㅋㅋ')

# 논리연산자

# num = int(input('1~10사이의 숫자를 입력하세요 : '))

# if 1 <= num <= 10:
#     print('내 말을 잘 이해했군')


# 조건문이 참일 때 실행할 명령이 2개 이상이면 아래쪽으로 명령을 계속 나열
# 들여쓰기가 맞게 써야 조건에 맞게 실행된다
# age = int(input('당신의 나이는? : '))
# if age < 30:
#     print('후후 아직 멀었다구')
#     print('서른이 되면 찾아보라구')


# else 다음에도 콜론이 있음
# num = int(input('10 이상의 숫자를 입력하세요 : '))

# if num < 10:
#     print('바보! 내말을 이해하지 못했니?')
# else:
#     print('제대로 입력했구나!! 입력한 값은 %d야' %num)

# elif문 : 조건이 만족하지 않을 때 다른 세부 조건을 하나 더 점검

# num = int(input('10 이상, 100 미만의 숫자를 입력하세요 : '))

# if num < 10:
#     print('바보! 내말을 이해하지 못했니?')

# elif num >= 100:
#     print('100 미만이라구!!')

# else:
#     print('제대로 입력했구나!! 입력한 값은 %d야' %num)

woman = True
age = 30
if woman == True:
    if age >= 30:
        print('멋진 여성의 길에 들어섰구나')