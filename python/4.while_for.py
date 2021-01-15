# 1. while문
# ryony = 1
# while ryony <= 5:
#     print(ryony, '번 요요를 한다')
#     ryony += 1


# num = 1
# sum = 0

# while num <= 100:
#     sum += num
#     num += 1
# print('sum =' ,sum)

# num = 151
# sum = 0

# while num <= 1500:
#     sum += num
#     num += 1
# print('sum = ', sum)

# 2. for문
# for student in [1,2,3,4,5]:
#     print(student, '번 학생이 도망갔네')

# range(시작, 끝, 증가값)
# 거꾸로
# for i in range (100, 0, -1):
#     print(i, '번째 학생은 어디로 간거야?')

# for i in range (1,51):
#     if i % 10 == 0:
#         print('+', end='')
#     else:
#         print('-',end='')

# for i in range(1, 51):
#     if i % 10 == 5:
#         print('+',end='')
#     else:
#         print('-',end='')

# break : 특정한 조건에 의해 탈출
# ex
age = [31, 23, 24, 41, 51, 62, 24, 13, 24, 53]

# for i in age:
#     if 20 <= i <= 70:
#         print('앞으로도 건강을 유지합시다!! 당신의 나이는 %d입니다' %i)

#     elif i < 20:
#         print('우앙 새나라의 어린이당')
#         break

# age 리스트 13 뒤의 24, 53은 출력되지 않는다

# continue : 이번 루프는 지나치고 다른 루프는 계속 수행
# for i in age:
#     if 20 <= i <= 70:
#         print('앞으로도 건강을 유지합시다!! 당신의 나이는 %d입니다' %i)

#     elif i < 20:
#         print('우앙 새나라의 어린이당')
#         continue
# age 리스트 13 뒤의 24, 53도 출력된다


# 이중루프
# for i in range(2, 20):
#     print('='*10)
#     print(i,'단')
#     print('='*10)
#     for q in range(2, 20):
#         print('%dx%d='%(i,q),i*q)


# dan = 2
# while dan <= 19:
#     hang = 2
#     print(dan, '단')
#     while hang <= 9:
#         print(dan, '*', hang, '=', dan*hang)
#         hang += 1
#     dan += 1
#     print()


# 무한 루프
# while True를 활용하여 무한 루프 작성
# 반복 조건이 항상 참이므로 이 루프는 무한 반복 -> 중간에 반드시 break 명령을 해야함

# print('4 x 8 = ?')
# while True:
#     a = int(input('정답을 입력하세요 : '))
#     if (a == 32) : 
#         break
# print('정답')

# 오프셋 : 기준점에서의 상대적 거리. 첫 요소의 오프셋이 0부터 시작하는 것이 좋다


# for i in range(0, 6):
#     for num in range(i*10, (i*10)+10):
#         print (num, end=',')
#     print()

# star = 1
# start = 0
# end = 10

# for i in range(end, start, -1):
#     print(' '*i,'*'* star, ' '*i)
#     print()
#     star += 2


def star_triangle(endline):
    star = 1
    for i in range(endline,0, -1):
        print(' ' * i, '*'*star, ' ' * i)
        star += 2


star_triangle(int(input("줄 수를 입력하세요")))
