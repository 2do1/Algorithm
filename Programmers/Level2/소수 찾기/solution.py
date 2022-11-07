from itertools import permutations

def solution(numbers):
    answer = 0
    
    for i in range(1, len(numbers) + 1):
        num_list = list(set(permutations(numbers, i))) # set 자료구조를 이용하여 중복 제거
        for num in num_list:
            if num[0] != "0": # 첫번째 수가 0이 아닐 경우
                num = int("".join(num)) # 합쳐준 후, 숫자형으로 변환
                if isPrimeNumber(num): # 소수일 경우
                    answer += 1

    return answer

def isPrimeNumber(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True