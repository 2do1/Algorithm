n = int(input()) # n번째 피보나치 수

# 0번째 피보나치 수: 0, 1번째 피보나치 수: 1
fibo = [0, 1]

def fibonacci(n):
    if n <= 1: # 0번째, 1번째일 경우
        return fibo[n]
    else:
        fibo_n = fibonacci(n - 1) + fibonacci(n - 2)
        fibo.append(fibo_n)
        return fibo_n

print(fibonacci(n)) # n번째 피보나치 수 출력

# 다른 사람의 풀이, 재귀 함수 이용
# n = int(input())
# def fibo(num):
#     if num<=1:
#         return num
#     return fibo(num-1)+fibo(num-2)
# print(fibo(n))

# 반복문 이용
# n = int(input())
# fibonacci = [0, 1]
# for i in range(2, n+1):
#     num = fibonacci[i-1] + fibonacci[i-2]
#     fibonacci.append(num)
# print(fibonacci[n])