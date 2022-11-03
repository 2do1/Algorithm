def solution(n, words):
    answer = []
    
    say_list = [words[0]] # 말한 단어들
    for i in range(1, len(words)):
        if words[i] in say_list: ## 이미 말한 단어일 경우
            answer.append(i % n + 1)
            answer.append(i // n + 1)
            break
        elif say_list[-1][-1] != words[i][0]: # 잘못된 단어를 말했을 경우
            answer.append(i % n + 1)
            answer.append(i // n + 1)
            break
        else: # 올바른 단어를 말했을 경우
            say_list.append(words[i])
    
    if not answer: # 탈락자가 발생하지 않았을 때
        answer = [0, 0]
        
    return answer