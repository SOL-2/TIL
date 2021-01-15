# dictionary : 키와 값의 쌍을 저장하는 대용량의 자료구조
dic = {'boy': '소년', 'girl':'소녀', 'school':'학교'}
print(dic)

# 키는 고유한 값을 가져야하지만 값은 중복되어도 상관없음
# 키는 읽기 전용이어서 변경할 수 없으며 튜플은 키로 쓸 수 있지만 리스트는 안됨

# get은 키가 없을 때 에러를 발생시키는 대신 None을 리턴하며 두번째 인수로 대신 돌려줄 디폴트값을 지정할 수 있음
# print(dic.get('student', '사전에 없는 단어입니다'))

# 키 in 사전 구문으로 사전에 있는 지 확인
# if 'student' in dic:
#     print('사전에 있는 단어입니다')

# else:
#     print('이 단어는 사전에 없습니다')


# dict의 삽입, 삭제, 수정 등의 편집
dic['boy'] = '남자애' # 키가 이미 존재하면 기존의 키 값을 변경한다
dic['woman'] = '여성'
del dic['school']
print(dic)

# keys, values, items 메서드 호출 : 키, 값, 키와 값의 쌍
# print(dic.keys())    # dict_keys(['boy', 'girl', 'woman'])
# print(dic.values()) # dict_values(['남자애', '소녀', '여성'])
# print(dic.items()) # dict_items([('boy', '남자애'), ('girl', '소녀'), ('woman', '여성')])

keyList = dic.keys()
for key in keyList:
    print(key)

# -> 진짜 리스트는 아니어서 append, insert등 편집함수 사용 x
# keyList = list(dic.keys()) 로 바꿔서 편집함수 사용해야 함


# 두 개의 사전을 병합할 때는 update 메서드
dic2 = {'student':'학생', 'teacher':'선생님', 'book':'책'}
dic.update(dic2)
# print(dic)
# {'boy': '남자애', 'girl': '소녀', 'woman': '여성', 'student': '학생', 'teacher': '선생님', 'book': '책'}

song = ''' Tonight
I just want to take you higher
Throw your hands up in the sky
Let's set this party off right '''


alphabet = dict()

for c in song:
    if c.isalpha()==False: # 알파벳이 아니면 넘어감
        continue
    c = c.lower()
    if c not in alphabet: # 알파벳 dict에 없으면 키를 넣고 값을 추가
        alphabet[c] = 1
    else:
        alphabet[c] += 1 # 알파벳 dict에 있으면 값만 추가

# print(alphabet)
key = list(alphabet.keys())
key.sort()

for c in key:
    num = alphabet[c]
    print(c, '->', num)


# 집합 : 값은 없고 키만 있다는 점
asia = { 'korea', 'china', 'japan', 'korea' } 
# print(asia)  # {'japan', 'china', 'korea'}
# 키의 중복을 허락하지 않으며 순서도 중요하지 않음