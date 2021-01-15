# 문자열 메서드
s = 'python programming'
print(len(s)) # len은 내장함수
print(s.find('o')) 
print(s.rfind('o')) # 뒤에서부터 검색
print(s.index('r'))
print(s.count('m')) # 부분 문자열도 검색할 수 있다
# 나머지는 메서드 : 클래스에 소속되어 있는 함수. 객체에 대해 특화된 작업 수행

# 있는 지 없는 지 알고 싶을 때는 in 구문 사용
print('a' in s)

# 앞부분의 일부를 비교할때는 startswith/ 마지막은 endswith
if s.startswith('python'):
    print('python입니다')

# ss = 'Good morning. my love cho.'

# print(ss.lower())
# print(ss.upper())
# print(ss)

# print(ss.swapcase())
# print(ss.capitalize())
# print(ss.title())

# 공백 제거
# sss = '   angel   '
# print(sss + '님')
# print(sss.lstrip()+'님') # 아예 공백이 안생김
# print(sss.rstrip()+'님')
# print(sss.strip()+'님')

# print(sss.lstrip(),'님') # ,를 쓰면 반칸정도 공백이 생김
# print(sss.rstrip(),'님')
# print(sss.strip(),'님')


# 일정한 폭 지정
price = [30, 13500, 2500]
for p in price:
    print('가격:%d원'%p)

# 가격:30원
# 가격:13500원
# 가격:2500원

for p in price:
    print('가격:%7d원'%p)

# 가격:     30원
# 가격:  13500원
# 가격:   2500원

for p in price:
    print('가격:%-7d원'%p)

# 가격:30     원
# 가격:13500  원
# 가격:2500   원

pie = 3.14159265
# print('%10f' %pie)
# print('%10.8f'%pie)
# print('%10.5f' %pie)
# print('%10.2f'%pie)
#   3.141593
# 3.14159265
#    3.14159
#       3.14


# 리스트
# 리스트에 소속되는 각각의 값을 요소 또는 원소
# 이중리스트
lol = [[1,2,3],[4,5],[6,7,8,9]]
# print(lol[0])  # [1, 2, 3]
# print(lol[2][1]) # 7


# for i in lol:
#     for q in i:
#         print(q,end=' ')
#     print()
# 1 2 3 
# 4 5 
# 6 7 8 9 

score = [
    [88,76,92,98],
    [65,87,92,76],
    [21,53,76,97],
    [99,26,88,92]
]

total = 0
totalsub = 0

for student in score:
    sum = 0
    for subject in student:
        sum += subject
    subjects =len(student) # 과목 갯수
    print('총점 %d, 평균 %.2f' %(sum, sum/subjects))
    total += sum
    totalsub += subjects
print('전체평균 %.2f' %(total/totalsub))
# 총점 354, 평균 88.50
# 총점 320, 평균 80.00
# 총점 247, 평균 61.75
# 총점 305, 평균 76.25
# 전체평균 76.62

# list comprehension
# [수식 for 변수 in 리스트 if 조건]

# nums = [n * 2 for n in range(1, 11)]
# for i in nums:
#     print(i,end =',')

# 2,4,6,8,10,12,14,16,18,20,

# append와 insert
num = [1,2,3,4]
num.append(5)
print(num)

num.insert(2,100)
print(num)

list1 = [1,2,3,4,5]
list2 = [10,11]
list1.extend(list2)
print(list1)

# 삭제 
list3 = [1,2,3,4,5,6,7,8,9,10]
list3.remove(10) # list 소속의 삭제 메서드
print(list3)
del(list3[0]) # 파이썬 키워드/ 메서드 아님
print(list3)
print(list3.pop()) # 인수가 없으면 마지막 요소를 삭제하여 리턴
# 선입선출할 때 사용
print(list3)

# 정렬
country = ['Korea', 'japan', 'CHINA', 'america']
country.sort()
print(country)
# ['CHINA', 'Korea', 'america', 'japan']
# 그냥 sort하면 대문자가 더 작은것으로 평가되어 앞쪽에 배치됨
country.sort(key=str.lower) # 대소문자 비교 시 sort에 key 인자
print(country)
# ['america', 'CHINA', 'japan', 'Korea']
# 요소 자체가 바뀌는 것은 아님

# sorted는 정렬하여 새로운 리스트를 반환함
# country2 = sorted(country)
# print(country2)


# tuple(튜플)
# 튜플은 편집할 수 없고 ()를 사용한다
# 튜플의 요소를 읽고 범위를 추출하여 잘라낼 수도 있고 연결하거나 요소를 반복할 수도 있음
# 튜플의 요소를 변경하거나 삭제하는 것은 불가능

# 여러 개의 변수에 값을 한꺼번에 대입하는 기능
# ex)
Tomato = '조을연', '장한솔', '문숙연'
cho, jang, moon = Tomato
# print(cho) # 조을연
# print(jang) # 장한솔
# print(moon) # 문숙연
# 세 개의 요소를 가지는 튜플을 정의하고 세 변수를 튜플로 만들어 튜플끼리 대입하면 대응되는  요소끼리 대입된다

# a, b = 12, 34
# print(a,b)
# a,b = b,a
# print(a,b)

import time

def gettime():
    now = time.localtime()
    return now.tm_hour, now.tm_min

result = gettime()
print(result)
print('지금은 %d시 %d분입니다' %(result[0],result[1]))

# divmod
d,m = divmod(7, 3)
print('몫', d)
print('나머지', m)
# 몫 2
# 나머지 1

# list <-> tuple 상호 변환 가능하지만 많은 시간이 소요됨
scoreLi = [89, 11, 85, 56, 79, 98]
tu = tuple(scoreLi)
print(tu)
li = list(tu)
print(li)
