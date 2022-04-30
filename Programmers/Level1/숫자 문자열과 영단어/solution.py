def solution(s):
    answer = 0 
    num_word_dict = {"zero": '0', "one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}
    
    for key, value in num_word_dict.items(): 
        if key in s: # 영단어가 있는경우 
            s = s.replace(key, value) # 숫자로 바g꿔준다
            
    answer = int(s) # int형으로 변환
    return answer