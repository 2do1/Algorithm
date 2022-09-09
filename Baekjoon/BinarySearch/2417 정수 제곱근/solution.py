n = int(input()) # 정수 n

start = 0
end = n

answer = 0 # q^2 ≥ n인 가장 작은 음이 아닌 정수 q

while start <= end:
    mid = (start + end) // 2

    if mid ** 2 >= n: # q^2 ≥ n일 경우
        answer = mid
        end = mid - 1
    else: 
        start = mid + 1
        
print(answer)

from math import ceil

n = int(input())

q = ceil(n ** 0.5)

print(q)