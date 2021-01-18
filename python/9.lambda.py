# lambda 
# 1) filter 함수 : 첫번째 인수 - 조건 지정, 두번째 인수 - 대상 리스트

def flunk(s):
    return s < 60

score = [45, 89, 72, 53, 94]
for s in filter(flunk, score):
    print(s)

# 2) map 함수 : 모든 요소에 대해 변환 함수를 호출하여 새 요소값으로 구성된 리스트를 생성
# 인수 구조는 필터 함수와 동일, 요소값을 어떻게 변경할 것인가는 첫번 째 인수로 전달된 변환 함수의 동작에 따라 달라진다

def half(s):
    return s / 2

# for s in map(half, score):
#     print(s, end=',')

def total(s, b):
    return s + b

# bonus = [2,3,0,0,5]
# for s in map(total, score, bonus):
#     print(s, end=',')


# lambda 함수
# filter, map 함수는 다른 함수를 인수로 받음. 이 함수를 호출 전 인수로 전달할 함수부터 정의해야함
# 이럴 때 간편하게 쓸 수 있는 게 람다식!!
# lambda 인수 : 식

# filter lambda식
for s in filter(lambda x: x < 60, score):
    print(s)

# for s in map(lambda x: x/2, score):
#     # print(s, end=',')



# list의 사본
# list1 = [1,2,3]
# list2 = list1

# list2[1] =100

# print(list1) [1, 100, 3]
# print(list2) [1, 100, 3]
# [1, 100, 3]
# [1, 100, 3]

# 두 리스트가 같은 메모리를 가리키고 있기 때문 -> copy 메서드로 복사본을 생성한다
# list1 = [1,2,3]
# list2 = list1.copy()   # list2 = list1[:] 이걸 써도 동일

# list2[1] = 100
# print(list1)
# print(list2)
# [1, 2, 3]
# [1, 100, 3]


import copy
list0 = ['a', 'b']
list1 = [list0,1,2]
list2 = copy.deepcopy(list1)

list2[0][1] ='c'
# print(list1)
# print(list2)
# [['a', 'b'], 1, 2]
# [['a', 'c'], 1, 2]

