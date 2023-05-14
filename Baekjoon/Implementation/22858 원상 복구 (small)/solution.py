n, k = map(int, input().split()) # 카드의 개수 N, 카드를 섞은 횟수인 K

s = list(map(int, input().split())) # k번 카드를 섞은 결과
d = list(map(int, input().split()))

for _ in range(k):
    p = [0] * n 
    for index in range(n):
        p[d[index] - 1] = s[index]
    s = p

print(*s)