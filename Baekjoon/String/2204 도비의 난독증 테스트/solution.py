while True:
    n = int(input()) # 단어의 개수

    if n == 0: # 마지막 입력일 경우
        break

    word_list = sorted([input() for _ in range(n)], key=lambda x : x.lower()) # 소문자를 바꾼 기준으로 정렬을 해준다.

    print(word_list[0]) # 사전상 가장 앞서는 단어 출력