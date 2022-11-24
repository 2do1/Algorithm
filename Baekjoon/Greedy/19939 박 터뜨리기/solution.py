n, k = map(int, input().split()) # n은 공, k는 바구니 개수

baskets = [basket for basket in range(1, k + 1)]
# baskets_sum = k * (k + 1) // 2

if sum(baskets) > n:
    print(-1)
elif (n - sum(baskets)) % k == 0:
    print(k - 1)
else:
    print(k)