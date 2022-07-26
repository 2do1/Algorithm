# 내 풀이
n, k = map(int, input().split()) 

answer = 0 # 1번 과정 또는 2번 과정을 수행해야 하는 최소 횟수

while True:
    if n == 1: # n이 1이 될 경우
        break

    if n % k == 0: # 나누어 떨어질 경우, 2번 연산
        answer += 1
        n //= k
    else: # 나누어 떨어지지 않을 경우, 1번 연산
        answer += 1
        n -= 1 

print(answer)


# 교재 풀이
# # N, K공백을 기준으로 구분하여 입력 받기
# n, k = map(int, input().split())

# result = 0

# while True:
#     # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
#     target = (n // k) * k
#     result += (n - target)
#     n = target
#     # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
#     if n < k:
#         break
#     # K로 나누기
#     result += 1
#     n //= k

# # 마지막으로 남은 수에 대하여 1씩 빼기
# result += (n - 1)
# print(result)