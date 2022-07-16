s = input() # 문자열 S

# 알파벳 개수 26개
# print(ord('a')) # 97
# print(ord('z')) # 122
# print(ord('A')) # 65
# print(ord('Z')) # 90

rot13 = ""
for char in s:
    if char.isupper(): # 대문자일 경우
        num = ord(char) + 13
        if num > 90: # 대문자 범위를 벗어났을 경우
            num -= 26
        rot13 += chr(num) # 문자로 다시 변환
    elif char.islower(): # 소문자일 경우
        num = ord(char) + 13
        if num > 122: # 소문자 범위를 벗어났을 경우
            num -= 26
        rot13 += chr(num)
    else: # 숫자 또는 공백일 경우
        rot13 += char
        
print(rot13)

# 처음 풀이
# rot13 = "" # S를 ROT13으로 암호환 내용
# for char in s:
#     if char == " ": # 공백일 경우
#         rot13 += " "
#     elif char.isdigit(): # 숫자일 경우
#         rot13 += char
#     else: # 소문자 또는 대문자일 경우
#         if 97 <= ord(char) <= 122: # 소문자일 경우
#             temp = ord(char)
#             for _ in range(13):
#                 temp += 1
#                 if temp == 123: # 소문자 범위를 벗어날 경우
#                     temp = 97
#             rot13 += chr(temp)
#         elif 65 <= ord(char) <= 90: # 대문자일 경우
#             temp = ord(char)
#             for _ in range(13):
#                 temp += 1
#                 if temp == 91:  # 대문자 범위를 벗어날 경우
#                     temp = 65
#             rot13 += chr(temp)

# print(rot13)