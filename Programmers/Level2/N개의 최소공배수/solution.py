def gcd(num1, num2):
    if num2 > num1:
        num1, num2 = num1, num2
        
    while num2 != 0:
        num1, num2 = num2, num1 % num2
        
    return num1

def lcm(num1, num2):
    lcm = num1 * num2 // gcd(num1, num2)
    
    return lcm
    
def solution(arr):
    
    answer = arr[0] 
    for i in range(1, len(arr)):
        answer = lcm(answer, arr[i])
        
    return answer