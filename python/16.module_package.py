# 1) module
# 변수, 함수를 재실행 할 수 있도록 스크립트를 여러 개의 파일로 나누어 작성하는 것
# 이 때 나누어진 스크립트 파일 -> 모듈

# 다른 모듈에서 불러와 사용할 때는 변수와 함수를 정의만 해야지 자신의 코드를 실행해서는 안됨
# 다른 모듈에 함수를 제공하는 모듈은 테스트 코드를 가질 수 있지만 직접 실행하기 보다는
# 호출할 때만 동작하는 것이 깔끔함
# 단독 실행 시에는 
# __name__ 변수는 실행 중인 모듈의 이름
# 단독 실행할 때는 '__main__'이고
# 다른 모듈에서 임포트하여 사용할 때는 모듈 자신의 이름인 util이 된다


# 모듈은 임포트하는 파일과 같은 디렉토리에 있어야 함

import sys
# sys.path # 디렉토리 경로의 리스트

path = '/Users/janghansol/TIL/Pystudy/'

# 디렉토리 경로에 임포트하는 파일이 있는 경로를 추가
sys.path.append(path)

import util

util.calcsum(10)


# 패키지
# 패키지 : 모듈을 관리하기 위한 상위의 개념 

sys.path.append(path + '/' + 'mypack')

# import mypack.calc.add
# mypack.calc.add.outadd(1,2)

# import mypack.report.table
# mypack.report.table.outreport()

# 간단하게 쓰기 위해서 from ~ import 구문 사용
# from mypack.calc import add
# add.outadd(1,2)

# from mypack.report import table
# table.outreport()




# from 패키지 import *
# 패키지에 포함된 모든 모듈을 임포트하는 문장

from mypack.calc import *
add.outadd(1,2) # NameError: name 'add' is not defined
multi.outmulti(1,2)

# 실행 시 add 모듈을 찾을 수 없다는 에러 발생
# 모든 모듈을 읽어오는 것은 프로그램의 반응성이 떨어짐
# 다른 패키지의 모듈과 이름 충돌이 발생할 수도 있음

# -> 패키지 디렉토리에 __init__.py파일을 작성해야 함 (3.3이후 필수 아님)
# 작성하고 실행하면 에러 안남



# 서드 파티 모듈
# print(sys.builtin_module_names)


# beautifulsoup4를 이용한 웹크롤링
# 가상환경 : python 3.7.0(data_env_TF2)