test_case = int(input()) # 테스트 케이스 개수

for _ in range(test_case):
    word_a, word_b = map(str, input().split())
    
    if len(word_a) != len(word_b): # 두 단어의 길이가 다를 경우
        print("{a} & {b} are NOT anagrams.".format(a=word_a, b=word_b))
    else: # 두 단어의 길이가 같을 경우
        word_a_list = sorted(word_a) # 오름차순 정렬 후 리스트로 리턴
        word_b_list = sorted(word_b) # 오름차순 정렬 후 리스트로 리턴

        if word_a_list == word_b_list: # 두 리스트가 같을 경우
            print("{a} & {b} are anagrams.".format(a=word_a, b=word_b))
        else: # 두 리스트가 다른 경우
            print("{a} & {b} are NOT anagrams.".format(a=word_a, b=word_b))