# 알파벳 소문자로만 이루어진 단어 S
s = input()

# 알파벳이 단어에 포함되어 있지 않다면 -1을 출력
alphabet_index_list = [-1] * 26 # 알파벳들이 처음 등장했을 때의 인덱스값들을 담아놓는 리스트

# print(ord('a')) 'a' -> 97
# print(ord('z')) 'z' -> 122

for alphabet in s:
    idx = ord(alphabet) - 97 # 아스키 코드로 변환 
    # if alphabet_index_list[idx] == -1: # 처음 등장했을 때의 인덱스값만을 담기 위해서
    alphabet_index_list[idx] = s.index(alphabet)
    
for alphabet_index in alphabet_index_list: # 알파벳 인덱스 출력
    print(alphabet_index, end = ' ')
# print(*alphabet_count_list, end = ' ') 

# 다른 사람의 풀이
# word = input()
# alphabet = list(range(97,123))  # 아스키코드 숫자 범위

# for x in alphabet :
#     print(word.find(chr(x))) 