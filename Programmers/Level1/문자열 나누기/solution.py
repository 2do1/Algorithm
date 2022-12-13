def solution(s):
    answer = 0
    
    while True:
        first_alphabet = s[0] # 첫 글자
        first_alphabet_count = 1 # 첫 글자 개수
        other_alphabets_count = 0 # 다른 글자들의 개수

        for index in range(1, len(s)):
            if s[index] == first_alphabet:
                first_alphabet_count += 1
            else:
                other_alphabets_count += 1
            
            if first_alphabet_count == other_alphabets_count: # 두 횟수가 같아지는 경우
                break
        
        if first_alphabet_count != other_alphabets_count: # 더이상 읽을 글자가 없다면
            answer += 1
            break  
        else:
            if len(s) <= first_alphabet_count + other_alphabets_count:
                answer += 1
                break
            else:
                answer += 1
                s = s[first_alphabet_count + other_alphabets_count:]
        
    return answer