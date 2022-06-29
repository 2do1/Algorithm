def solution(s):
    answer = ''
    s_length = len(s) # 단어 s의 길이
    mid = s_length // 2
    
    if s_length % 2 == 0: # 단어의 길이가 짝수일 경우
        answer = s[mid - 1:mid + 1]
    else: # 단어의 길이가 홀수일 경우
        answer = s[mid]
        
    return answer