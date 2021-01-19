mylist = [[1], [2]]
mylist2 = [[1,2,3],[4,5]]

# 1번째 풀이 - 문제 잘못 이해
# count = list()
# for i in mylist:
#     for q in i:
#         count.append(q)
#         print(count)

# 2번째 풀이 
count = 0
for i in mylist:
    for q in i:
        print(q)
    

     



# def solution(mylist):
#     answer = list()
#     for i in mylist:
#         for q in i:
#             answer.append(0)

#     print(answer)
#     answer = mylist[0]
#     return answer

# solution(mylist)


# def solution(mylist):
#     answer = mylist[0]
#     return answer

 