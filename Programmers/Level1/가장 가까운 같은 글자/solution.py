def solution(s):
    answer = []
    
    alphabets = [] # 알파벳 담을 리스트
    
    for alphabet in s:
        if alphabet not in alphabets: 
            answer.append(-1)
            alphabets.append(alphabet)
            continue
        answer.append(len(alphabets) - (len(alphabets) - alphabets[::-1].index(alphabet)) + 1)
        alphabets.append(alphabet)
    
    
    return answer