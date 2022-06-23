import sys
sys.setrecursionlimit(5000000) # 재귀 제한조건을 풀어준다.

# def factorial(n): # 팩토리얼 반복을 통해 구현
#     total = 1
#     for i in range(2, n + 1):
#         total *= i
    
#     return total

def factorial(n): # 팩토리얼 재귀를 통해 구현
    if n == 1: # 숫자가 1일 경우
        return 1
    return n * factorial(n - 1)

n = int(input())
factorial_num = str(factorial(n))[::-1] # 거꾸로 뒤집어준다 -> 가장 낮은 자리수부터

for num in factorial_num:
    if num == '0': # 0일 경우
        continue
    print(num) # 0이 아닌, 가장 낮은 자리수 출력
    break