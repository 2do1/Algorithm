# 처음 내 풀이
n = int(input()) # 단어의 개수 n
group_word_count = 0 # 그룹 단어의 개수

for _ in range(n):
    group_word = True # 그룹 단어인지의 여부를 나타내는 변수
    word = input()
    if len(word) == 1: # 단어 길이가 1일 경우
        group_word_count += 1
        continue 

    alphabet_list = [] # 각 단어를 구성하는 알파벳들을 담을 리스트
    
    for alphabet in word:
        if len(alphabet_list) == 0: # 리스트가 비어있을 경우
            alphabet_list.append(alphabet)
            continue

        if alphabet in alphabet_list and alphabet != alphabet_list[-1]: # 알파벳이 떨어져 나타나는 경우
            group_word = False # 그룹 단어가 아니다.
            break
        
        alphabet_list.append(alphabet)

    if group_word: # 그룹 단어일 경우
        group_word_count += 1

print(group_word_count)

# 다른 사람의 풀이
# 이 풀이가 더 좋은 풀이인것 같다.
# N = int(input())
# result = N
# for _ in range(0, N):
#     word = input()
#     for j in range(0, len(word)-1):
#         if word[j] == word[j+1]:
#             continue
#         elif word[j] in word[j+1:]:
#             result -= 1
#             break
# print(result)