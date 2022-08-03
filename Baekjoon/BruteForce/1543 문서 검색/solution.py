doc = input() # 문서
word = input() # 검색하고 싶은 단어

doc = doc.replace(word, 'X' * len(word))
answer = doc.count('X' * len(word))

print(answer)

# 다른 사람의 풀이
# doc = input()
# word = input()
# count = 0
# i = 0
# while i <= len(doc) - len(word):
#     if doc[i:i + len(word)] == word:
#         count += 1
#         i += len(word) 
#     else:              
#         i += 1         
# print(count)
    
# 실패한 코드
# doc = input() # 문서
# word = input() # 검색하고 싶은 단어

# total = 0 # 중복되지 않게 몇 번 등장

# for i in range(len(doc) - 1):
#     for j in range(i + 1, len(doc)):
#         if doc[i:j] == word: # 검색하는 단어일 경우
#             total += 1
#             doc = doc[j:] # 단어가 등장한 위치의 이후부터 탐색
#             break

# print(total)