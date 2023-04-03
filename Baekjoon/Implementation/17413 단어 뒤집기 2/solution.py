s = input()

answer = ""

index = 0
while index < len(s):

    if s[index] == '<': # 왼쪽 괄일 경우
        while True:
            if s[index] == '>':
                answer += s[index]
                index += 1
                break
            answer += s[index]
            index += 1

    elif s[index] == " ": # 빈칸일 경우
        answer += " "
        index += 1
    else:
        word = ""
        while True:
            if index == len(s) - 1:
                word += s[index]
                index += 1
                break
            elif s[index] == " " or s[index] == "<":
                break
            word += s[index]
            index += 1
            
        answer += word[::-1]


print(answer)

# 스택 자료구조를 이용한 다른 사람의 풀이
# string = input().rstrip()
# word_stack = []
# tag = False
# res = ''

# for s in string:
#     # 공백이면 word_stack 비움
#     if s == " ":
#         while word_stack:
#             res += word_stack.pop()
#         res += s

#     # 태그 안 단어는 뒤집지 않음
#     elif s == "<":
#         while word_stack:
#             res += word_stack.pop()
#         tag = True
#         res += s

#     elif s == ">":
#         tag = False
#         res += s

#     elif tag:
#         res += s

#     # 태그 밖 단어는 뒤집음
#     else:
#         word_stack.append(s)

#     # print(res, tag)

# # 출력
# while word_stack:
#     res += word_stack.pop()
# print(res)