# 단어는 대문자와 소문자로만 이루어져있다.
word = input() # 단어 입력받는다.

answer = "" # 대문자 -> 소문자, 소문자 -> 대문자로 바꾼 단어

for alphabet in word: # 각 알파벳마다 접근한다.
    if alphabet.islower(): # 알파벳이 소문자일 경우
        answer += alphabet.upper() # 대문자로 변경
    else: # isupper(), 대문자일 경우
        answer += alphabet.lower() # 소문자로 변경

print(answer)

# 풀이 1(처음에 작성한 코드))
# 알파벳 아스키 코드 값 범위 
# print(ord('A')) -> 65
# print(ord('Z')) -> 90

# print(ord('a')) -> 97
# print(ord('z')) -> 122

# for alphabet in word: # 각 알파벳마다 접근한다.
#     if 65 <= ord(alphabet) <= 90: # 대문자일 경우
#         answer += alphabet.lower() # 소문자로 변경
#     elif 97 <= ord(alphabet) <= 122: # 소문자일 경우
#         answer += alphabet.upper() # 대문자로 변경

# print(answer)


# 풀이 2
# 대문자는 소문자로, 소문자는 대문자로 변환해주는 함수.
# word.swapcase() 
# print(word)