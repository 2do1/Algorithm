n, k = map(int, input().split()) # n개의 원소, 최대 k번의 바꿔치기 연산

a = sorted(map(int, input().split())) # 배열 a, 오름차순 정렬
b = sorted(map(int, input().split()), reverse=True) # 배열 b, 내림차순 정렬

for i in range(k): # k번 바꿔치기
    if a[i] < b[i]: # b의 원소가 a의 원소보다 클 때
        a[i], b[i] = b[i], a[i] # 스와프

print(sum(a)) # a의 모든 원소의 합의 최댓값