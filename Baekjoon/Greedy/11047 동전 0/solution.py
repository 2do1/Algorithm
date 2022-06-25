# n 동전의 종류, k 가치의 합
n, k = map(int, input().split())

coin_list = sorted([int(input()) for _ in range(n)], reverse=True) # 오름차순으로 주어짐 -> 내림차순으로 정렬해준다.

answer = 0 # 필요한 동전 개수의 최솟값
for coin in coin_list: # 동전의 가치가 큰 것부터 접근
    if k >= coin: # 남은 가치의 합이 동전 가치 이상일경우
        answer += k // coin
        k %= coin
    else: # 남은 가치의 합이 동전 가치 보다 작을 경우
        continue

print(answer)