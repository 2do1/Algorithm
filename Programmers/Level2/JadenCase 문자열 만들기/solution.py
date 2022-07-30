def solution(s):
    answer = []
    
    s = s.split(" ")

    for word in s:
        if word == "": # 공백일 경우
            answer.append(word)
        else: # 공백이 아닐 경우
            temp = ""
            if word[0].isdigit(): # 첫 문자가 숫자일 경우
                temp += word[0]
            else: # 첫 문자가 알파벳일 경우
                temp += word[0].upper() 
            temp += word[1:].lower() # 첫 문자를 제외하곤 다 소문자로 바꿔준다.
            answer.append(temp)
            
    answer = " ".join(answer)
                
    return answer