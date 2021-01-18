# 모듈 : 파이썬 코드를 작성해 놓은 스크립트 파일
# 이 안에 함수, 변수, 클래스 등이 정의

# import 모듈명 : 모듈에 작성된 모든 상수와 함수를 다 가져온다
# 모듈의 함수를 호출할 때 모듈명.함수() 이렇게 불러와야 한다

# 특정 함수만 불러올 때는
# from 모듈 import 함수명


import math

print(math.sin(math.radians(45))) # 삼각함수 sin 45
print(math.sqrt(2)) # 제곱근
print(math.factorial(5)) # 5의 계승


import turtle as t

# t.penup()
# t.goto(-720,0)
# t.pendown()
# for x in range(-720, 720):
#     t.goto(x, math.sin(math.radians(x))*100)
# t.done()


# statistics(통계)

# median : 중앙값, 짝수인 경우 보간값을 계산
# median_low(high) : 중앙값, 집합내의 낮은값(높은값)을 구함
# median_grouped : 그룹 연속 중앙값을 구함

# mode : 최빈값

# pstdev : 모표준편차
# stdev : 표준편자
# variance : 분산

import statistics

score = [30,40,60,70,80,90]

# print(statistics.mean(score))
# print(statistics.harmonic_mean(score))
# print(statistics.median(score))
# print(statistics.median_low(score))
# print(statistics.median_high(score))



# 시간
import time
# t = time.time()
# print(time.ctime(t))

t = time.localtime()
print('%d년 %d월 %d일 %d시 %d분' %(t.tm_year,t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))

import datetime

now = datetime.datetime.now()
print('%d년 %d월 %d일 %d시 %d분' %(now.year, now.month, now.day, now.hour, now.minute))


# 실행 시간 측정
# 두 지점 간의 경과 시간을 측정할 수 있음

# start = time.time()
# for a in range(1000):
#     print(a)

# end = time.time()
# print(end - start)


# sleep 함수 : 지정한 시간만큼 CPU를 잠재워 시간을 끈다

# print('안녕하세요')
# time.sleep(1)
# print('최최차차는 무슨 뜻일까용?')
# time.sleep(5)
# print('최애는 최애 차은우는 차은우!!!')


import calendar

# 캘린더가 직접 프린트된다
# print(calendar.calendar(2021))
# print(calendar.month(2021,1))

week = ['월','화', '수', '목','금', '토', '일']
day = calendar.weekday(2021,8,15)
print('광복절은', week[day] + '요일이다.')




# random(난수)

import random

# for i in range(5):
#     print(random.random())  # 무작위 난수 추출


# for i in range(5):
#     print(random.randint(1,100)) # start, end(end는 제외)


# for i in range(5):
#     print(random.uniform(1,100)) # 실수 난수 추출

# 15.58221365751854
# 37.634979308902004
# 62.1169080091983
# 93.45233552642958
# 86.50909702127441


food = ['짜장면', '짬뽕', '샌드위치', '순댓국']

# print(random.choice(food))

random.shuffle(food)
# print(food)
# 리스트 순서를 섞어줌



# 산수문제 내기

# a = random.randint(1,11)
# b = random.randint(1,11)

# question = '%d + %d = ?' %(a,b)

# c = int(input( question))

# if question == c:
#     print('정답입니다.')
# else:
#     print('틀렸습니다.')


# 산수문제 2
# correct = 0

# while True:
#     a = random.randint(1,10)
#     b = random.randint(1,10)

#     question = '%d + %d = ? (끝낼때는 0)' %(a,b)
#     c = int(input(question))

#     if c == 0:
#         break

#     elif c == a + b:
#         print('정답입니다')
#         correct = correct + 1

#     else:
#         print('틀렸습니다')

# print('%d 개 맞췄습니다.' % correct)


# # 숫자 맞추기 게임

# answer = random.randint(1,101)

# while True:
#     num = int(input('숫자를 입력하세요(끝낼 때는 0) : '))

#     if num == 0:
#         break

#     elif num == answer:
#         print('정답입니다 : %d ' %answer)
#         break

#     elif num < answer:
#         print('너무 작아요 ㅜㅜ 다시 시도해보세요!!')
        
#     else:
#         print('너무 커요 ㅜㅜ 다시 시도해보세요!!')


# 숫자 맞추기 게임 2
# 카운트 셀 때는 루프 들어가기 전에 입력 받을 때마다 1씩 증가

count = 0
answer = random.randint(1,101)


while True:
    num = int(input('숫자를 입력하세요(끝낼 때는 0) : '))

    if num == 0:
        break
    count += 1

    
    if num == answer:
        print('%d만에 맞췄습니다 답은 %d입니다 ' %(count,answer))
        break

    elif num < answer:
        print('너무 작아요 ㅜㅜ 다시 시도해보세요!!')
        
    else:
        print('너무 커요 ㅜㅜ 다시 시도해보세요!!')