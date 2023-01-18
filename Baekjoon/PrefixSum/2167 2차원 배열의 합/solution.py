n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

prefix_sums = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix_sums[i][j] = prefix_sums[i - 1][j] + prefix_sums[i][j - 1] - prefix_sums[i - 1][j - 1] + matrix[i - 1][j - 1]

k = int(input())

for _ in range(k):
    i, j, x, y = map(int, input().split())

    print(prefix_sums[x][y] - prefix_sums[i - 1][y] - prefix_sums[x][j - 1] + prefix_sums[i - 1][j - 1])