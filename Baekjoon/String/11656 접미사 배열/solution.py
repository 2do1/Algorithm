s = input() # 문자열 s

suffix_list = sorted([s[i:] for i in range(len(s))]) # 접미사 리스트 오름차순, 사전순으로 정렬

for suffix in suffix_list: # 접미사 출력
    print(suffix)