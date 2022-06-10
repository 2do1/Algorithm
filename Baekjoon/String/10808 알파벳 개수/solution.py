# 알파벳 소문자로만 이루어진 단어 S
s = input()

alphabet_count_list = [0] * 26 # 알파벳의 개수를 담을 리스트

# print(ord('a')) 'a' -> 97
# print(ord('z')) 'z' -> 122

for alphabet in s:
    # idx = ord(alphabet) % 97
    idx = ord(alphabet) - 97 # 아스키 코드로 변환 
    alphabet_count_list[idx] += 1
    
for alphabet_count in alphabet_count_list: # 알파벳 개수 출력
    print(alphabet_count, end = ' ')
# print(*alphabet_count_list, end = ' ') 