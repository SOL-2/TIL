# 파일 입출력을 위해 위치를 확인하고 버퍼를 준비 -> 오픈
# open(파일경로, 모드)

# 파일 열기, 쓰기, 닫기
# f = open('live.txt', 'wt')
# f.write(''' 삶이 그대를 속일지라도
# 슬퍼하거나 노하지 말라!
# 우울한 날들을 견디면
# 믿으라, 기쁨의 날이 오리니''')
# f.close()

# 경로 지정 없이 파일명만 주었기 때문에 현재 디렉토리에 생성된다

# 파일 읽기
# try:
#     f = open('live.txt', 'rt')
#     text = f.read()
#     print(text)

# except FileNotFoundError:
#     print('파일이 없습니다')

# finally:
#     f.close()



# read 함수는 한번에 읽을 수 있지만 대용량 파일을 읽을 때는 메모리를 많이 소모함

# 읽을 양을 지정해서 read 함수의 인수로 읽을 때
# f = open('live.txt', 'rt')

# while True:
#     text = f.read(10)
#     # text의 길이가 0이면 -> 파일을 다 읽었으면
#     if len(text) == 0:
#         break
#     print(text, end='')
# f.close



# readline 함수 : 한 줄씩 읽으며 파일 마지막에 도달하면 빈 문자열을 리턴
# 빈 줄을 읽을 때까지 반복하면 모든 줄을 순서대로 다 읽는다₩
# f = open('live.txt', 'rt')
# text = ''
# line = 1

# while True:
#     row = f.readline()
#     if not row:
#         break
#     text += str(line) + ' : ' + row
#     line += 1

# f.close()
# print(text)


# endline은 각 줄 끝에 개행 문자가 포함되어 있음
# 따로 개행 문자를 출력하지 말아야 함
# f = open('live.txt','rt')
# rows = f.readline()

# for row in rows:
#     print(row, end='')

# f.close()


# 입출력 위치
# 파일 객체는 다음 입출력 위치를 정확하게 기억한다. 그래서 조금씩 반복적으로 읽어도 전체 파일을 다 읽을 수 있다
# -> 순차 접근(처음부터 끝까지 다 읽어 메모리 로드)

# 입출력 위치를 바꿔가며 파일의 원하는 부분을 자유롭게 액세스하는 방식 -> 임의접근
# tell함수 호출, 위치 변경할 때는 seek 함수 사용
# seek(위치, 기준)
# 기준이 0이면 파일 처음부터, 2면 끝에서부터, 1이면 현재 위치를 기준


# 내용 추가
# 'a'모드는 파일에 내용 추가. 기존 내용을 그대로 유지하고 뒤에 내용을 덧붙임
# 'w'모드는 덮어쓰고 새로 만듦

# f = open('live.txt', 'at')
# f.write('\n\nby. 푸쉬킨.')
# f.close() 

# 파일 입출력이 끝나면 반드시 close 함수로 닫아야  읽기 모드로 다시 열 수 있음
# 파일을 확실하게 닫기 위해 with 블록 사용

# with open('live.txt', 'rt') as f:
#     text = f.read()
# print(text)



###################
# 파일 관리
# os / shutil 모듈

# live.txt 파일 복사
import shutil

# shutil.copy('live.txt', 'live2.txt')


# 디렉토리 관리 함수

# 테스트 디렉토리에 파일을 생성해둠
# f = open('/Users/janghansol/TIL/test/test_1.txt','wt')
# f.write('''테스트입니다용
# 기억하세요
# 읽을 필요없어용''')
# f.close()

# shutil 모듈을 활용하여 복사
path = '/Users/janghansol/TIL/test/'

# shutil.copy(path + 'test_1.txt', path + 'test_2.txt')
# shutil.copy(path + 'test_1.txt', path + 'ryoni.txt')
# shutil.copy(path + 'test_1.txt', path + 'sol2.txt')


import os

files = os.listdir(path)

# for file in files:
#     print(file)

# test_2.txt
# test_1.txt
# ryoni.txt
# sol2.txt


def dumpdir(path):
    files = os.listdir(path)
    for file in files:
        # 패스 뒤에 '/' 있으면 패스 뒤에 파일명만 붙이고
        if path[ -1] == '/':
            fullpath = path + file

        # 패스 뒤에 '/' 없으면 패스 뒤에 '/' 붙이고 파일명 붙이기
        else:
            fullpath = path + '/' + file
        # print(fullpath)

        # isdir : 폴더인지 확인하는 함수
        if os.path.isdir(fullpath):
            print('[' + fullpath + ']')
            dumpdir(fullpath)   # 재귀함수 : 자신을 다시 호출

        else:
            print('\t' + fullpath)


# dumpdir(path)

# [/Users/janghansol/TIL/test/test2020]
#         /Users/janghansol/TIL/test/test2020/test_2.txt
#         /Users/janghansol/TIL/test/test2020/test_1.txt
# [/Users/janghansol/TIL/test/test2021]
#         /Users/janghansol/TIL/test/test2021/ryoni.txt
#         /Users/janghansol/TIL/test/test2021/sol2.txt



