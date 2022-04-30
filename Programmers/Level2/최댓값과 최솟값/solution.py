def solution(s):
    answer = ''
    s_list = s.split() # 공백을 기준으로 나눠준다.
    # num_list = []
    
    # for num in s_list:
    #     num_list.append(int(num))
    
    num_list = [int(num) for num in s_list] # int형으로 변환후 리스트에 넣어준다.
    
    answer = str(min(num_list)) + " " + str(max(num_list)) # int형에서 str형으로 다시 변환.
    
    return answer