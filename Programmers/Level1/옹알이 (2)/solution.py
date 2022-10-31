def solution(babbling):
    answer = 0
    
    say_list = ["aya", "ye", "woo", "ma"] # 말할 수 있는 발음들 
    
    for word in babbling:
        for say in say_list:
            if say * 2 not in word: # 연속된 발음이 없을 경우
                word = word.replace(say, "X" * len(say))
                    
        if word == len(word) * "X": # 말할 수 있는 발음일 경우
            answer += 1
        
    return answer