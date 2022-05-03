def solution(n):
    answer = 0
    num_sum = 0 # 숫자들의 합
    
    for i in range(1, n + 1): # i : 1 ~ n
        for j in range(i, n + 1): # j: i ~ n
            num_sum += j
            if num_sum == n: # 숫자들의 합이 자연수 n과 같을 경우
                answer += 1
                num_sum = 0 # 다른 경우의 수를 판단하기 위해 다시 0으로 초기화해준다.
                break
            elif num_sum > n: # 숫자들의 합이 자연수 n보다 클경우
                num_sum = 0 # 다른 경우의 수를 판단하기 위해 다시 0으로 초기화해준다.
                break
    return answer