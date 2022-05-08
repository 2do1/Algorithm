def solution(s):
    answer = ''

    new_word_list = [] # 새로운 문자열 담을 리스트
    
    # word_list = s.split() -> 틀림
    # 하나 이상의 공백 문자로 구분되어있으니, 공백문자에 대해서도 처리해줘야함
    word_list = s.split(" ") 
    for word in word_list:
        new_word = "" # 바꿀 새로운 문자열
        for i in range(len(word)):
            if i % 2 == 0: # 단어별 인덱스가 짝수일 경우
                new_word += word[i].upper() # 대문자로
            else: # 단어별 인덱스가 홀수일 경우
                new_word += word[i].lower() # 소문자로
        new_word_list.append(new_word)
        
    answer = " ".join(new_word_list) # 공백을 기준으로 합쳐준다.
    
    # idx = 0 # 단어별 인덱스
    # for i in range(len(s)):
    #     if s[i] == " ": # 공백일경우
    #         answer += " "
    #         idx = 0 # 한 단어가 끝났으므로 다시 0으로 초기화해준다.
    #     else:
    #         if idx % 2 == 0: # 단어별 인덱스가 짝수일 경우
    #             answer += s[i].upper() # 대문자로
    #             idx += 1
    #         else: # 단어별 인덱스가 홀수일 경우
    #             answer += s[i].lower() # 소문자로
    #             idx += 1
                
    return answer