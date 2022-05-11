def solution(n):
    answer = 0
    
    # 정수 n의 절반을 넘어가는 값들은 계산할 필요가 없다.
    answer = n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0]) 

    return answer

    # 처음 작성한 코드
    # divisor_list = [i for i in range(1, n+1) if n % i == 0] # n의 약수들을 담을 리스트
    # answer = sum(divisor_list) # 모든 약수들의 합