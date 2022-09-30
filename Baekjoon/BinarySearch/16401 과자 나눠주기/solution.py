m, n = map(int, input().split()) # 조카 수 m, 과자 수 n

snack_list = list(map(int, input().split())) # 과자의 길이

start = 1
end = max(snack_list)
answer = 0 # 막대과자의 최대 길이

while start <= end:
    mid = (start + end) // 2
 
    total = 0 # 줄 수있는 막대 과자의 수
    for snack in snack_list:
        total += snack // mid

    if total >= m: # 조카의 수보다 막대 과자의 수가 많을 경우
        answer = mid
        start = mid + 1
    else: # 조카의 수보다 막대 과자의 수가 적을 경우
        end = mid - 1

print(answer)

# python3에서는 시간초과, pypy3에서 정답
import sys

m, n = map(int, sys.stdin.readline().split()) # 조카 수 m, 과자 수 n

snack_list = sorted(map(int, sys.stdin.readline().split())) # 과자의 길이

start = 1
end = snack_list[-1]
answer = 0 # 막대과자의 최대 길이

while start <= end:
    mid = (start + end) // 2
 
    total = 0 # 줄 수있는 막대 과자의 수
    for snack in snack_list:
        total += snack // mid

    if total >= m: # 조카의 수보다 막대 과자의 수가 많을 경우
        answer = mid
        start = mid + 1
    else: # 조카의 수보다 막대 과자의 수가 적을 경우
        end = mid - 1

print(answer)