k, n = map(int, input().split()) # 이미 갖고 있는 랜선의 개수 k, 필요한 랜선 n

k_list = sorted([int(input()) for _ in range(k)]) # 이미 가지고 있는 랜선들

start = 1
end = k_list[-1]
answer = 0 # 랜선의 최대 길이

while start <= end:
    mid = (start + end) // 2
    
    total = 0 # 잘라서 만든 랜선의 총 개수
    for k in k_list:
        total += k // mid
    
    if total >= n:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
        
print(answer)