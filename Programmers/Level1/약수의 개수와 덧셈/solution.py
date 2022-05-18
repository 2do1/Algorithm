def solution(left, right):
    answer = 0 
    
    for num in range(left, right + 1):
        divisor_count = 1 # 각 숫자의 약수의 개수, 자기 자신도 약수이기 때문에 1로 초기값 설정.
        for i in range(1, num // 2 + 1): # 절반까지만 약수인지 확인.
            if num % i == 0: # 약수일 경우
                divisor_count += 1
                
        if divisor_count % 2 == 0: # 약수의 개수가 짝수일 경우
            answer += num
        else: # 약수의 개수가 홀수일 경우
            answer -= num
                
    return answer
    
    # 다른 사람의 풀이 -> 각 수의 정수 제곱근이 존재한다면 약수의 개수가 홀수이다.
    # answer = 0
    # for x in range(left, right+1):
    #     if math.sqrt(x) == int(math.sqrt(x)):
    #         answer -= x
    #     else:
    #         answer += x
    # return answer