# 예외 처리

# try:
#     실행할 명령

# except 예외 as 변수:
#     오류 처리문

# else:
#     예외가 발생하지 않을 때의 처리

# ex) 
# 점수를 int형으로 입력해야하는데 str으로 입력했을 때
# str = '89점'
# try :
#     score = int(str)
#     print(score)

# except:
#     print('예외가 발생했습니다')

# print('작업완료')


# while True:
#     str = input('점수를 입력하세요 : ')
#     try:
#         score = int(str)
#         print('입력한 점수 : ', score)
#         break
#     except:
#         print('점수 형식이 잘못되었습니다.')

# print('작업완료')




# raise 명령 : 고의적으로 예외를 발생
# 작업을 위한 선결 조건이 맞지 않거나 더 이상 진행할 수 없는 치명적인 문제가 발생했을 때
# 호출원으로 예외를 던져 잘못됐음을 알림

# ex) 입력값이 음수일 때
# def calcsum(n):
#     if(n < 0):
#         raise ValueError
#     sum = 0
#     for i in range(n+1):
#         sum = sum + i
#     return sum

# try:
#     print('~10 =', calcsum(10)) # ~10 = 55
#     print('~-5 =', calcsum(-5)) # 입력값이 잘못되었습니다.
# except ValueError:
#     print('입력값이 잘못되었습니다.')




# def calcsum(n):
#     if (n < 0):
#         return -1

#     sum = 0
#     for i in range(n+1):
#         sum = sum + i
#     return sum

# result = calcsum(10)
# if result == -1:
#     print('입력값이 잘못되었습니다')
# else:
#     print('~10 =', result)

# result = calcsum(-5)
# if result == -1:
#     print('입력값이 잘못되었습니다')
# else:
#     print('~10 =', result)


# dictionary에서의 예외처리 (get 함수 사용)
# dic = {'boy': '소년', 'girl': '소녀', 'school': '학교'}

# search = input('찾는 단어가 있으신가요? : ')

# 찾는 단어가 없을 때
# try:
#     print(dic[search])

# except:
#     print('찾는 단어가 없습니다')


# result = dic.get(search)

# if (result == None):
#     print('찾는 단어가 없습니다')

# else:
#     print(result)




# finally 블록
# 예외 발생 여부와 상관없이 반드시 실행해야 할 명령을 지정
# 메모리나 자원을 할당한 후 해제 -> fimally 블록에 작성

# try:
#     print('네트워크 접속')
#     a = 2 / 0
#     print('네트워크 통신 수행')
# finally:
#     print('접속 해제')
# print('작업 완료')

#  파일은 with 구문 사용

# assert : 프로그램의 현재 상태가 맞는 지 확인
# assert 조건, 메시지
score = 128
assert score <= 100, '점수는 100 이하여야 합니다'
print(score)
