word = input() # 알파벳 소문자로만 이루어진 단어

if word == word[::-1]: # 팰린드롬일 경우
    print(1)
else: # 팰린드롬이 아닐 경우
    print(0)

# 다른 사람의 풀이 
# word = list(str(input()))

# if list(reversed(word)) == word:
#     print(1)
# else:
#     print(0)