def solution(number, limit, power):
    answer = 0
    
    for num in range(1, number + 1):
        divisor_num = count_divisor(num)
        if divisor_num > limit:
            answer += power
            continue
        answer += divisor_num
        
    return answer

def count_divisor(num):
    total = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            total += 1
            if i ** 2 < num:
                total += 1            
    return total