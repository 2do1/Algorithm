n = int(input()) # 단어의 수

word_list = [input() for _ in range(n)]

for word in word_list:
    if word[::-1] in word_list: # 비밀 번호일 경우
        print(len(word), word[len(word) // 2]) # 비밀번호 길이와 가운데 글자 출력
        break

    # 뒤에 조건이 앞에 조건을 포함하고 있어서 조건을 따로 안적어도 된다.
    # if word == word[::-1] or word[::-1] in word_list: # 비밀 번호일 경우
    #     print(len(word), word[len(word) // 2]) # 비밀번호 길이와 가운데 글자 출력
    #     break