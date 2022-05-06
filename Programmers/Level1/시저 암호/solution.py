def solution(s, n):
    answer = ''
    
    for alphabet in s:
        if alphabet == " ": # 공백일 경우
            answer += alphabet
        else: # 공백이 아닐 경우
            ascii_alphabet = ord(alphabet) # 각 알파벳 아스키코드 값으로 변환한다.
            for i in range(n): # n만큼 민다.
                if ascii_alphabet == 90: # 대문자 Z일 경우
                    ascii_alphabet = 65 # 대문자 A로 변경
                elif ascii_alphabet == 122: # 소문자 z일 경우
                    ascii_alphabet = 97 # 소문자 a로 변경
                else:
                    ascii_alphabet += 1
                
            answer += chr(ascii_alphabet) # 알파벳으로 다시 변환
    return answer

# 다른 사람 풀이 
# def caesar(s, n):
#     s = list(s)
#     for i in range(len(s)):
#         if s[i].isupper():
#             s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
#         elif s[i].islower():
#             s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

#     return "".join(s)