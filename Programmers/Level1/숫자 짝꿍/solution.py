def solution(X, Y):
    answer = ''
    
    for i in range(9, -1, -1):
        num = str(i) # 문자열로 변환해준다.
        
        x_count = X.count(num) # X에 있는 숫자의 개수
        y_count = Y.count(num) # Y에 있는 숫자의 개수
        
        if x_count > 0 and y_count > 0: # 공통으로 나타나는 정수가 있을 경우
            if x_count > y_count: # X가 더 많이 갖고 있을 경우 
                answer += num * y_count
            else: # 개수가 동일하거나, Y가 더 많이 갖고 있을 경우
                answer += num * x_count
        
    if not answer: # 공통으로 나타나는 정수가 없을 경우
        answer = "-1"
    elif answer[0] == "0": # 공통으로 나타나는 정수 중 첫번째가 "0"일 경우
        answer = "0"

    return answer