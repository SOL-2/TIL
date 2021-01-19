# 테이블 생성

# 상용 DBMS는 DB와 테이블 디자인을 위한 툴을 제공
# SQLite는 별도의 툴이 없으며 스크립트로 DB를 생성한다

# makeDB

import sqlite3

# con = sqlite3.connect('addr.db')
# cursor = con.cursor()

# cursor.execute('DROP TABLE IF EXISTS tblAddr')
# cursor.execute(''' CREATE TABLE tblAddr
#     (name CHAR(16) PRIMARY KEY, phone CHAR(16), addr TEXT)''')

# cursor.execute('INSERT INTO tblAddr VALUES ("김상형", "123-4567", "오산")')
# cursor.execute('INSERT INTO tblAddr VALUES ("조을연", "123-1324", "이천")')
# cursor.execute('INSERT INTO tblAddr VALUES ("장한솔", "123-2435", "홍천")')


# con.commit()

# cursor.close()
# con.close()


###############################


# select db
# SELECT : 모든 필드를 읽어서 덤프

# con = sqlite3.connect('addr.db')
# cursor = con.cursor()

# cursor.execute('SELECT * FROM tblAddr') # 테이블의 모든 필드를 다 읽는다는 뜻
# table = cursor.fetchall() # fetchall : 모든 레코드를 한꺼번에 읽어 리스트로 리턴하며 읽을 것이 없으면 빈 리스트를 돌려줌
# for record in table: # record는 튜플 형태
#     print('이름 : %s, 전화 : %s, 주소 : %s' %record)

# cursor.close()
# con.close()

# fetchall : 한꺼번에 다 읽음. 커서의 배열 크기 제한이 있어 너무 큰 배열은 메모리를 많이 소모
# fetchone : 한 레코드씩 순서대로 읽음

# select db2

# con = sqlite3.connect('addr.db')
# cursor = con.cursor()

# cursor.execute('SELECT * FROM tblAddr')
# while True:
#     record = cursor.fetchone()
#     if record == None:
#         break
#     print('이름 : %s, 전화 : %s, 주소 : %s '%record)

# cursor.close()
# con.close()

# 레코드 하나를 읽으며 반복적으로 호출하면 다음 레코드를 계속 읽어줌
# 더 읽을 레코드가 없으면 None을 리턴.
# 무한루프를 돌며 더 이상 읽을 레코드가 없을 때까지 반복하면서 순서대로 읽게됨

# ORDER BY : 레코드를 읽는 순서 지정, 해당 필드를 기준으로 오름차순으로 정렬
# 내림차순으로 정렬 시 뒤에 DESC를 붙인다

# con = sqlite3.connect('addr.db')
# cursor = con.cursor()

# cursor.execute('SELECT * FROM tblAddr ORDER BY addr')
# table = cursor.fetchall()
# for record in table:
#     print('이름 : %s, 전화 : %s, 주소 : %s' %record)

# cursor.close()
# con.close()


# WHERE : 조건을 지정하여 원하는 레코드만 검색 
# 특정 필드의 값이나 대소 관계에 따라 조건에 맞는 레코드만 검색

# 이름이 '장한솔'인 사람의 필드만 읽어 전화번호를 출력

# con = sqlite3.connect('addr.db')
# cursor = con.cursor()

# # SELECT 필드 FROM 레코드명 WHERE 조건
# cursor.execute('SELECT phone FROM tblAddr WHERE name = "장한솔"')
# record = cursor.fetchone()
# print('장한솔의 전화번호는 %s 입니다' %record)

# cursor.close()
# con.close()


# 수정 및 삭제
# 특정 필드 값을 수정할 때는 UPDATE 

# con = sqlite3.connect('addr.db')
# cursor = con.cursor()

# cursor.execute('UPDATE tblAddr SET addr = "서울" WHERE name = "장한솔"')

# con.commit()

# cursor.close()
# con.close()

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute('SELECT * FROM tblAddr')
while True:
    record = cursor.fetchone()
    if record == None:
        break

    print('이름 : %s, 전화번호 : %s, 주소 : %s' %record)

cursor.close()
con.close()