# Variabel 
# 1. 형식

a = 12
b = 13
print (a, b)
# 12 13

# seperator 함수 사용
# 1) 다른 문자로 바꿔보기
print(a,b, sep = '&')
# 12&13

# 2) 공백없이 
print(a,b, sep='')
# 1213

# 3) 긴 문자열로 바꿔보기
print(a,b, sep='---->')
# 12---->13

# 예시
s = '서울'
d = '대전'
g = '대구'
b = '부산'
print(s,d,g,b, sep='찍고 ') 
# 서울찍고 대전찍고 대구찍고 부산

# print 명령의 end 인수는 내용을 출력한 후 더 출력할 문자를 지정하는데 
# 이 값이 개행 문자로 되어있어 한번 호출할 때마다 자동 개행된다
# end 인수를 다른 문자로 지정하면 개행 코드 대신 이 문자가 출력
# -> 즉 end를 빈 문자열로 지정하면 내용만 출력하고 아무것도 출력하지 않아 연이은 print 호출

dog = '강아지'
cat = '고양이'
print(dog)
print(cat)
# 강아지
# 고양이

print(dog, end ='')
print(cat) 
# 강아지고양이

# 2. 입력
# name = input('이름이 뭐니? ')
# print(name)
# 입력한 값을 name 변수에 받았음

# 입력한 값은 str타입. 계산을 하기 위해서는 int형으로 변경
# price = input('가격을 입력하세요 : ')
# num = input('개수를 입력하세요 : ')
# sum = int(price) * int(num)
# print('총액은', sum, '원입니다.')

# price = int(input('가격을 입력하세요 : '))
# num = int(input('개수를 입력하세요 : '))
# sum = price * num
# print('총액은', sum, '원입니다.')

# 3. 변수명
# 변수 : 메모리에 이름을 붙여 놓고 값을 저장하는 것
# 변수는 변할 수 있는 값이어서 언제든 다른 값으로 바꿀 수 있음

# a = 100
# print(a)
# a = 200
# print(a)

# 별도의 선언 절차 없이 대입하는 값에 따라 타입이 결정된다
# 가급적이면 처음 정한 용도대로 사용하는 것이 좋다

# 타입 조사할 때는 type 명령
# print(type(a)) # <class 'int'>
# a = 'hansol'
# print(type(a)) # <class 'str'>

# 3. 수치형
# 3-1. 정수형(int)
# 음수를 표현할 수 있지만 소수점 이하 값은 표현할 수 없음
# a = 0x1a
# print(a) # 16진수 0x1a 는 10진수 26

# print(hex(26)) # 0x1a
# print(oct(26)) # 0o32
# print(bin(13)) # 0b1101

# 3-2. 실수형(float)
# 소수점 이하의 수를 표현할 수 있음
# 엄청 큰 값은 부동 소수점 방식으로 표기
# 영문자 E, 또는 e를 가운데 두고 왼쪽에 가수, 오른쪽에 지수를 쓴다
# ex) 9조 4600억 => 9.46*10의 12승 => 9.46e12

# 3-3. 복소수형(complex)
# 제곱해서 음수가 되는 가상의 숫자
# 실수부 + 허수부j
# a = 1+2j
# b = 3+4j
# print(a + b)
# 복소수.real은 실수부, 복소수.image는 허수부를 리턴
# 복소수.conjugate 켤레 복소수
# abs 함수는 복소수의 절대값


# 4. 문자열(str)
# Escape Sequence

print('I Say \'Help\' to you')
print('I Say \nHelp to you') 
# 진짜 문자로서의 \를 쓰고 싶을 땐 \\ 이렇게 두 번 써준다

# 경로 출력 시 \\ 두번 쓰기 귀찮으니 r 접두를 붙인다
# print(r"c:\temp\nex.txt")

# 원래 문자열은 중간에 두 행으로 나누어 쓸 수 없음
# 긴 문자열을 정의할 때는 따옴표 세 개 
# 중간에 개행되더라도 하나의 문자열로 정의
s = '''강나루 건너서 밀밭 길을 구름에 달 가듯이 가는 나그네
길은 외줄기 남도 삼백리 술익는 마을마다 타는 저녁놀
구름에 달 가듯이 가는 나그네'''
print(s)

# 또는 매 줄 마다 escape 문자열 사용
ss = '강나루 건너서 밀밭 길을 구름에 달 가듯이 가는 나그네\n'
'길은 외줄기 남도 삼백리 술익는 마을마다 타는 저녁놀\n'
'구름에 달 가듯이 가는 나그네' 

# ord / chr 함수
# ord함수는 문자의 코드를 조사하고 chr함수는 코드로부터 문자를 구한다

print(ord('a')) # 97
print(chr(98)) # b
for c in range(ord('A'), (ord('Z') + 1)):
    print(chr(c), end='')

# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# A 부터 Z까지 정수를 반복하며 chr함수를 활용하여 문자로 변환하여 출력

# 4. 진위형(boolean)
# 참, 거짓을 표현
