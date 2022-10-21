s = input() # 문자열 S

answer = set()  # 서로 다른 부분 문자열
for i in range(len(s)):
    for j in range(i, len(s)):
        answer.add(s[i:j + 1])
        
print(len(answer)) # 서로 다른 부분 문자열의 개수

# 시간 초과 
# s = list(input()) # 문자열 S

# answer = []  # 서로 다른 부분 문자열
# for i in range(len(s)):
#     for j in range(i, len(s)):
#         temp = s[i:j + 1]
#         if temp not in answer: # 서로 다른 부분 문자열일 경우
#             answer.append(temp)

# print(len(answer)) # 서로 다른 부분 문자열의 개수