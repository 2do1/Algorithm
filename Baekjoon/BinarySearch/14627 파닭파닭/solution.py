import sys

s, c = map(int, input().split()) # 파의 개수 s, 파닭의 수 c

s_list = sorted([int(sys.stdin.readline().rstrip()) for _ in range(s)]) # 파의 길이

start = 1
end = s_list[-1]
answer = 0 # 라면에 넣을 파의 양

while start <= end:
    mid = (start + end) // 2 # 파의 길이

    total = 0 # 만들 수 있는 파의 총 개수 
    for s in s_list:
        total += s // mid

    if total >= c: # 파의 개수가 파닭의 수 이상일 경우
        start = mid + 1
        answer = sum(s_list) - c * mid # 라면에 넣을 파의 양
    else: # 파의 개수가 파닭의 수보다 적을 경우
        end = mid - 1

print(answer)