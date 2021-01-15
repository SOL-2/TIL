# 비슷한 코드가 반복된다면 정의해 놓고 계속 사용하는 것이 좋음

def calcsum(n):
    sum = 0
    for num in range(n+1):
        sum += num
    return sum

#  print(calcsum(100))

# 매개변수, 인수 : 호출원에서 함수로 전달되는 작업거리, 호출하는 쪽과 함수를 연결한다는 의미

def calrange(start, end):
    sum = 0
    for num in range(start, end+1):
        sum += num
    return sum
# print(calrange(5, 100))

# 리턴값 : 함수의 실행 결과를 호출원으로 돌려주는 값 (출력값)
# 리턴값이 꼭 있어야 하는 것은 아니며 반환할 값이 없는 경우도 있음
# 리턴이 없는 경우
def printsum(n):
    sum = 0
    for num in range( n + 1):
        sum += num
    print('~', n, '=', sum)

# printsum(4)
# printsum(10)
# 리턴값이 없는 함수는 단독으로만 호출
# 변수에 대입하거나 수식 내에서 사용해서는 안된다


# pass : 아무 동작도 하지 않음


# 인수의 형식
# 1) 가변 인수
# 함수를 호출할 때 형식 인수 개수만큼 실인수를 전달해야 한다
# 가변인수는 임의 개수의 인수를 받는다. 인수 이름앞에 * 기호를 붙이면 여러 개의 인수가 올 수 있다

# ex
def intsum(*ints):
    sum = 0
    for num in ints:
        sum += num
    return sum

# print(intsum(1,2,3))
# print(intsum(5,6,7,8,9,10))

# 가변 인수는 모든 인수를 다 포함하기 때문에 인수 목록의 마지막에 와야 한다
# intsum(s, *ints) -> 가능
# intsum(*ints, s) -> 에러
# initsum(*ints, *nums) -> 에러

# 인수목록에 기본값을 지정해둘 수 있어 생략 가능하다
def calstep(start, end, step =1):
    sum = 0
    for num in range(start, end+1, step):
        sum += num
    return sum

# print(calstep(1,10,1))
# print(calstep(1,10))


# 키워드 인수
# 함수를 호출할 떄 함수 정의문에 선언된 순서대로 실인수를 전달하며 호출문에 나타나는 순서에 따라 형식 인수에 차례대로 대입된다
# 순서대로 인수를 전달하는 방식을 Positional Argument
# 순서와 무관하게 인수를 전달하는 방법을 Keyword Argument(키워드 인수)라고 한다

def calcstep(begin,end, step):
    sum = 0
    for num in range(begin, end+1, step):
        sum += num
    return sum

# print(calcstep(3,5,1))
# print(calcstep(begin=1, step=2, end=10))

# 키워드 가변 인수 : 키워드 인수를 가변 개수 전달할 때는 인수 목록에 ** 기호를 붙인다
# 호출원에서 여러 개의 키워드 인수를 전달하면 인수의 이름과 값의 쌍을 사전으로 만들어 전달
# ex)
def calcstep1(**args):
    begin = args['begin']
    end = args['end']
    step = args['step']

    sum = 0
    for num in range(begin, end+1, step):
        sum += num
    return sum

# print(calcstep1(begin=3, end=11, step=2))


# 변수의 범위
# 1) 지역 변수 : 함수 내부에서 선언하는 변수
# 지역 변수는 함수 안에서만 사용됨

# 2) 전역 변수 : 함수 바깥에서 선언하는 변수
# 어디에서나 참조할 수 있다

# 함수 내부에서는 지역 변수가 우선!!
# 전역 변수임을 알려 주어야 할 때 사용하는 명령이 global
# ex)
price = 1000

def sale():
    global price
    price = 500

# sale()
# print(price)



# docstring : 함수 사용법이나 인수의미, 주의 사항등을 문서로 남김
def calcstep2(**args):
    '''begin에서 end까지의 수를 더해 return합니다 '''
    begin = args['begin']
    end = args['end']
    step = args['step']

    sum = 0
    for num in range(begin, end+1, step):
        sum += num
    return sum

help(calcstep1)