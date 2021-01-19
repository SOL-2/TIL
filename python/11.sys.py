import sys

# print('버전 :', sys.version)
# print('플랫폼 :', sys.platform)

# if (sys.platform == 'win32'):
#     print(sys.getwindowsversion())
# print('바이트 순서 : ' , sys.byteorder)
# print('모듈 경로 : ', sys.path )
# sys.exit(0) # 프로그램 강제 종료. 인수로 종료 코드를 지정하는데 0이면 정상종료. 그 외의 값이면 에러에 의한 종료. 생략 시 0이 적용


# 경과일 계산

import time

if (len(sys.argv) != 2):
    print('시작 날짜를 yyyymmdd로 입력하세요.')
    sys.exit(0)

birth = sys.argv[1]
if(len(birth) != 8 or birth.isnumeric() == False):
    print('날짜 형식이 잘못되었습니다.')
    sys.exit(0)

tm = (int(birth[:4]), int(birth[4:6]), int(birth[6:8]), 0,0,0,0,0,0)
ellapse = int((time.time() - time.mktime(tm)) / (24 * 60 * 60))
print(ellapse)



# 경과일 계산 2
year = int(input('태어난 년도를 입력하세요(4자리) : '))
month = int(input('태어난 월을 입력하세요 : '))
day = int(input('태어난 일을 입력하세요 : '))

tm = (year, month, day, 0, 0, 0, 0, 0, 0)
ellapse = int((time.time() - time.mktime(tm)) / (24 * 60 * 60))
print(ellapse)