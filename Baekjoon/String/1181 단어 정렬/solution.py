n = int(input())
word_list = []

for i in range(n):
    word = input()
    if word not in word_list: # 중복제거를 위해
        word_list.append(word)

word_list = sorted(word_list, key=lambda x : (len(x), x)) # 문자열 길이가 짧은것부터, 사전순 순서로 정렬

for word in word_list:
    print(word)