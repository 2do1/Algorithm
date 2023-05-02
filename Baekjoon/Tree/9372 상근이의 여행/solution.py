import sys

t = int(input())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split()) # 국가의 수 N, 비행기의 종류 M

    tree = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        tree[a].append(b)
        tree[b].append(a)

    print(n - 1)