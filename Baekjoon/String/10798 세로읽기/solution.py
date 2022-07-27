word_list = [list(input()) for _ in range(5)] # 다섯줄의 입력

max_length = len(sorted(word_list, key=lambda x : len(x))[-1]) # 가장 긴 글자의 길이

for i in range(max_length):
    for j in range(5):
        if i < len(word_list[j]): # 해당 글자가 존재할 경우
            print(word_list[j][i], end='')
        else: # 해당 글자가 존재하지 않을 경우
            continue