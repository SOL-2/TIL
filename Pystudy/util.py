INCH = 2.54

def calcsum(n):
    sum = 0
    for num in range(n + 1):
        sum += num
    return sum

# print('인치 =', INCH)
# print('합계 =', calcsum(10))

if __name__ == '__main__':
    print('인치 = ', INCH)
    print('합계 = ', calcsum(10))

# __name__ 변수는 실행 중인 모듈의 이름
# 단독 실행할 때는 '__main__'이고
# 다른 모듈에서 임포트하여 사용할 때는 모듈 자신의 이름인 util이 된다